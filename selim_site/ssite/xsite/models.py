from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from PIL import Image
import fitz  # PyMuPDF
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')
    bio = models.TextField(blank=True)
    is_authorized = models.BooleanField(default=False)  # Kullanıcının yetkili olup olmadığını belirler

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name



class Product(models.Model):
    name = models.CharField(max_length=200)
    subname = models.CharField(max_length=1000, null=True, blank=True)
    price = models.FloatField()  # FloatField olarak kalabilir
    digital = models.BooleanField(default=False, null=True, blank=True)
    pimage = models.ImageField(upload_to='img/', null=True, blank=True)
    #pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    discount = models.IntegerField(default=0)  # Discount as an integer
    apply_discount = models.BooleanField(default=False, null=True, blank=True)  # Discount flag
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        """
        Calculate and return the discounted price if the discount is active.
        """
        if self.apply_discount and self.discount > 0:
            return round(Decimal(self.price) * Decimal(1 - self.discount / 100), 2)
        return self.price
    

    @property
    def pimageURL(self):
        try:
            url = self.pimage.url
        except:
            url = ''
        return url


    @property
    def pdfURL(self):
        try:
            url = self.pdf.url
        except:
            url = ''
        return url
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"{self.product.name} - {self.image.name}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

# Create your models here.
class xsite(models.Model):
    # model alanları
    pass


class Category(models.Model):
    # model alanları
    pass
