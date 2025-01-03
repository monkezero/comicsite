from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView
from django.views.generic import TemplateView,DetailView
from ssite.forms import RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views import View


class CustomLoginView(LoginView):
    template_name = 'xsite/login.html'

class BookDetailView(DetailView):
    model = Product  
    template_name = 'xsite/book.html'  
    context_object_name = 'product' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context['product']
        context['images'] = product.images.all()  
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'xsite/product_detail.html'  
    context_object_name = 'product'

class CartView(ListView):
    model = Product
    template_name = 'xsite/cart.html' 
    context_object_name = 'products' 

class HomeView(ListView):
    model = Product 
    template_name = 'xsite/home.html'
    context_object_name = 'products'


class GetQuerySetView(View):
    def get(self, request):
        query = request.GET.get('q')
        if query:
            products = Product.objects.filter(
                Q(name__icontains=query)  
            )
        else:
            products = Product.objects.all()  
        return render(request, 'xsite/checkout.html', {'products': products})


class CheckoutView(ListView):
    model = Product
    template_name = 'xsite/checkout.html'
    context_object_name = 'products'

    def get(self, request):
        query = request.GET.get('q')
        if query:
            products = Product.objects.filter(
                Q(name__icontains=query)  
            )
        else:
            products = Product.objects.all()  
        return render(request, 'xsite/checkout.html', {'products': products})
    

class loginView(ListView):
    model = Product
    template_name = 'xsite/login.html'
    context_object_name = 'products'
    
class bookView(ListView):
    model = Product
    template_name = 'xsite/book.html'
    context_object_name = 'products'

class RegisterView(FormView):
    template_name = 'xsite/register.html'
    form_class = RegisterForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()  # Kullanıcıyı kaydet
        return super().form_valid(form)

class informationView(ListView):
    model = Product
    template_name = 'xsite/information.html'
    context_object_name = 'products' 

class bagView(ListView):
    model = Product
    template_name = 'xsite/bag.html'
    context_object_name = 'products' 