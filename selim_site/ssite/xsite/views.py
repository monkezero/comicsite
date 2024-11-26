from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView
from django.views.generic import TemplateView,DetailView

from django.contrib.auth import login, authenticate

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'xsite/login.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'xsite/product_detail.html'  # Oluşturacağınız HTML şablon
    context_object_name = 'product'

class CartView(ListView):
    model = Product
    template_name = 'xsite/cart.html' 
    context_object_name = 'products' 

class HomeView(ListView):
    model = Product
    template_name = 'xsite/home.html'
    context_object_name = 'products'

class CheckoutView(ListView):
    model = Product
    template_name = 'xsite/checkout.html'
    context_object_name = 'products'

class loginView(ListView):
    model = Product
    template_name = 'xsite/login.html'
    context_object_name = 'products'
    
class bookView(ListView):
    model = Product
    template_name = 'xsite/book.html'
    context_object_name = 'products'

class register_view(ListView):
    model = Product
    template_name = 'xsite/register.html'
    context_object_name = 'products'

class informationView(ListView):
    model = Product
    template_name = 'xsite/information.html'
    context_object_name = 'products' 

class bagView(ListView):
    model = Product
    template_name = 'xsite/bag.html'
    context_object_name = 'products' 