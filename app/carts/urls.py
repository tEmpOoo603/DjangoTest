from django.urls import path
from carts import views

app_name = 'cart'

urlpatterns = [
    path('cart-add/', views.cart_add, name='cart_add'),
    path('cart-remove/', views.cart_remove, name='cart_remove'),
    path('cart-change/', views.cart_change, name='cart_change'),
]
