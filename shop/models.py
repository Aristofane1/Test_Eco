from django.db import models
from django.contrib.auth.models import User
import datetime
from cart.cart import Cart

# Create your models here.

class Customer(models.Model):
	#user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


"""class Order(models.Model):
	customer = 
	date_ordered = 
	complete = 
	transation_id = 
"""

class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	promotion = models.FloatField(null=True)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=False,default=False, blank=True)
	categorie = models.CharField(max_length=200, null=True)
	#slug = models.SlugField(max_length=100, null = True, unique=True)
	detail = models.TextField(null=True)
	#post_heure = models.DateTimeField (auto_now_add = True)
	
	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url



class CartItem(models.Model):
	products = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return self.product.name


"""class Cart(models.Model):
	#items = models.ManyToManyField(CartItem, null=True, blank=True)
	product_list = models.ManyToManyField(Product, null=True, blank=True)
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

	def __str__(self):
		return self.products.name

"""


"""
class OrderItem(models.Model):
	product = 
	order = 
	quantity = 
	date_added =
"""

class ShippingAdress(models.Model):
	#customer = models.OneToOneField(Customer, null=True, blank=True, on_delete=models.CASCADE)
	#order = models.ManyToManyField(Cart, null=True, blank=True)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zipcode = models.IntegerField()
	#date_added = 


