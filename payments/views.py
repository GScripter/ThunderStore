from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from cart.cart import Cart
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'https://thunderstore.up.railway.app'
        if settings.DEBUG:
            YOUR_DOMAIN = 'http://localhost:8000'
        cart_products = Cart(request).session['cart']
        total = 0
        for cart, number in enumerate(cart_products):
            total += int(cart_products[number]['quantity']) * float(cart_products[number]['price'])
        total = total * 100
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data':{
                        'currency':'brl',
                        'unit_amount': int(total),
                        'product_data':{
                            'name': 'Thunder Store',
                        },
                    },
                    'quantity':1,
                }
            ],
                mode='payment',
                success_url=YOUR_DOMAIN + f'/create/order/client/{kwargs["id"]}',
                cancel_url=YOUR_DOMAIN + '/pagina/cancelado',
            )
        return redirect(checkout_session.url, code=303)

