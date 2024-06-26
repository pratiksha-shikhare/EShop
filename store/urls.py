from django.contrib import admin
from django.urls import path
from .views import home, signup
from .views.login import Login,logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware
urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login',Login.as_view(), name='login'),
    path('logout',logout, name='logout'),
    path('cart',Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]