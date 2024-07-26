from django.urls import path
from goods import views as goods

app_name = 'catalog'

urlpatterns = [
    path('', goods.catalog, name='index'),
    path('product/<int:product_id>/', goods.product, name='product'),
]