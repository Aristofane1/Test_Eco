from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
#from django.http import HttpResponse
#import datetime

def home(request):
	products = Product.objects.all()
	context = {'products' : products}
	return render(request,'shop/home.html', context)

""""def cart(request):
	cart = Cart.objects.all()[0]
	context = {"cart" : cart}
	return render(request,'shop/cart.html', context)
"""

#@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


#@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


#@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


#@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
	context = {}
	return render(request, 'shop/cart.html', context)
	
"""def update_cart(request, cart_id):
	cart = Cart.objects.all()[0]
	try:
		product = get_object_or_404(Product, pk=cart_id)
	except Product.DoesNotExist:
		pass
	except:
		pass
	if not product in cart.product_list.all():
		cart.product_list.add(product)
	else:
		cart.product_list.remove(product)

	return redirect('shop/cart.html')"""

def product(request, product_id):
	detail = get_object_or_404(Product, pk=product_id)
	#plus = []
	context = {'product_detail' : detail.detail,
				'product_categorie' : detail.categorie,
				'product_price' : detail.price,
				'product_promotion' : detail.promotion,
				'product_name' : detail.name,
				'product_image' : detail.imageURL,

	}
	return render(request,'shop/product.html', context)

def search(request):
	query = request.GET['query']
	if not query:
		product = Product.objects.all()
	else:
		product = Product.objects.filter(name__icontains=query)
	if not product.exists():
		product = Product.objects.filter(price__icontains=query)

	if not product.exists():
		product = Product.objects.filter(categorie__icontains=query)


	context = {'product' : product}
	return render(request,'shop/search.html', context)

def checkout(request):
	context = {}
	if request.method == "POST":
		address = request.POST['address']
		city = request.POST['city']
		state = request.POST['state']
		zipcode = request.POST['zipcode']
		country = request.POST['country']

		info_user = ShippingAdress(address=address,city=city,state=state,zipcode=zipcode)
		info_user.save()
		return render(request, 'shop/product.html')
	return render(request,'shop/checkout.html', context)

def user_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request,'shop/checkout.html')
		else:
			return render(request,'registration/login.html', locals())
	else:
		return render(request,'registration/login.html')


def sign_in(request):
	if request.method == "POST":
		try:
			username = request.POST.get('username')
			email = request.POST.get('email', False)
			password1 = request.POST.get('password1')
			password2 = request.POST.get('password2', False)
			if password1==password2:
				user = User.objects.create_user(username,email,password1)
				customer = Customer(username=username, email=email)
				customer.save()
				
				return render(request,'registration/login.html')
		except:
			return render(request,'registration/register.html')

	else:
		return render(request,'registration/register.html', locals())
