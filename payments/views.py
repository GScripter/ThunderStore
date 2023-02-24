from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from cart.cart import Cart
import stripe
from . models import Item, Order
from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'https://thunderstore.up.railway.app'
        if settings.DEBUG:
            YOUR_DOMAIN = 'http://localhost:8000'
        # Salvar produtos do carrinho na lista.
        line_items = []
        cart_products = Cart(request).session['cart']
        for cart, number in enumerate(cart_products):
            name = str(cart_products[number]['name'])
            if len(name) >= 20:
                name = str(cart_products[number]['name'])[:20]
                name+=str('...')
            line_items+=[{
                'price_data':{
                    'currency':'brl',
                    'unit_amount': int(float(cart_products[number]['price']))*100,
                    'product_data':{
                        'name': name,
                    },
                },
                'quantity': int(cart_products[number]['quantity']),
            }]
        # Criar seção de pagamento.
        user = User.objects.get(id=self.request.user.id)
        checkout_session = stripe.checkout.Session.create(
            customer_email = user.email,
            line_items = line_items,
            mode='payment',
            success_url=YOUR_DOMAIN + f'/pagina/pedido/sucesso/',
            cancel_url=YOUR_DOMAIN + '/pagina/pedido/cancelado/',
        )
        # Criar order
        create_order = Order.objects.create(checkout_session_id=checkout_session['id'], user_id=user.id, username=user.username, cpf=user.cpf, cep=user.cep,
                                            state=user.state, city=user.city, address=user.address,
                                            district=user.district, number=user.number, complement=user.complement)
        cart_products = Cart(request).session['cart']
        for cart, number in enumerate(cart_products):
            Item.objects.create(order_id=create_order.id, name=cart_products[number]['name'],
                                quantity=cart_products[number]['quantity'],
                                price=cart_products[number]['price'])
        cart_products = Cart(request)
        cart_products.clear()
        return redirect(checkout_session.url, code=303)


class OrderCompleteHook(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
        event = None
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
        # Handle the checkout.session.completed event
        if event['type'] == 'checkout.session.completed':
            session_id = event['data']['object']['id']
            order = Order.objects.filter(checkout_session_id=session_id).first()
            order.checkout_session_id = event['data']['object']['payment_intent']
            order.save()
        elif event['type'] == 'payment_intent.succeeded':
            session_id = event['data']['object']['id']
            order = Order.objects.filter(checkout_session_id=session_id).first()
            order.is_paid = True
            order.save()
        return HttpResponse(status=200)

