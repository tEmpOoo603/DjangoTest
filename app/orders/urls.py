from django.urls import path
from orders import views

app_name = 'order'
urlpatterns = [
    path('create-order', views.CreateOrderView.as_view(), name='create_order')
]