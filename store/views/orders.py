from django.views import View
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.orders import Order
# from store.models.category import Category
# from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
class OrderView(View):

    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        return render(request,'orders.html',{'orders':orders})