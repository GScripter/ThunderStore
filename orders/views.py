from django.shortcuts import render
from . models import Item, Order
from cart.cart import Cart
from users.models import User

# Create your views here.
def create_order(request, id):
    user = User.objects.get(id=id)
    create_order = Order.objects.create(user_id=user.id, username=user.username, cpf=user.cpf, cep=user.cep,
                                        state=user.state, city=user.city, address=user.address,
                                        district=user.district, number=user.number, complement=user.complement)
    order = Order.objects.filter(username=user.username)[0:1]
    cart_products = Cart(request).session['cart']
    for cart, number in enumerate(cart_products):
        Item.objects.create(order_id=order[0].id, name=cart_products[number]['name'],
                            quantity=cart_products[number]['quantity'],
                            price=cart_products[number]['price'])
    cart_products.clear()
    return render(request, 'order_success.html')

