from django.urls import path
from goods import views as goods

app_name = 'catalog'

urlpatterns = [
    path('<slug:category_slug>/', goods.catalog, name='index'),
    path('<slug:category_slug>/<int:page>/', goods.catalog, name='index'),
    path('<slug:category_slug>/<slug:product_slug>/', goods.product, name='product'),
]