"""
URL configuration for ssite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from .views import register
from .views import profile_view, add_product, delete_product
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("acconts/",include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('xsite.urls')),
    path('cart/', views.cart, name='cart'),
    path('information/', views.information, name='information'),
    path('checkout/', views.checkout, name='checkout'), 
    path('bag/', views.bag, name='bag'),
    path('book/', views.book, name='book'),
    path('login/', views.login, name='login'),
    path('register/', register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile_view, name='profile'),
    path('product/add/', add_product, name='add_product'),
    path('product/delete/<int:product_id>/', delete_product, name='delete_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
