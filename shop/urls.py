from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('login', views.user_login, name='login'),
    path('register', views.sign_in, name='sign_in'),
    path('accounts/', include('django.contrib.auth.urls')),
	#path('cart', views.cart, name='cart'),
    #path('cart/update/<int:cart_id>', views.update_cart, name='update_cart'),
	path('product/<int:product_id>', views.product, name='product'),
	path('checkout', views.checkout, name='checkout'),
    path('search', views.search, name='search'),


    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/',views.cart_detail,name='cart_detail'),
]

