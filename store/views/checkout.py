from django.views import View
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.orders import Order
# from store.models.category import Category
# from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address,phone,customer,cart,products)

        for product in products:
            order = Order(customer=Customer(id=customer),product=product,price=product.price,address=address,phone=phone,quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        return redirect('cart')