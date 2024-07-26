from django.urls import path
from goods import views as goods

app_name = 'catalog'

urlpatterns = [
    path('<slug:category_slug>/', goods.catalog, name='index'),
    path('product/<slug:product_slug>/', goods.product, name='product'),
]