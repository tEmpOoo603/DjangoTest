from django.urls import path
from goods import views as goods

app_name = 'catalog'

urlpatterns = [
    path('', goods.catalog, name='index'),
    path('product/<slug:product_slug>/', goods.product, name='product'),
]