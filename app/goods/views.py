from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from goods.models import Products, Categories


def catalog(request, category_slug):
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'all':
        goods = Products.objects.all().select_related('category')
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug).select_related('category'))
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)
    page = request.GET.get('page',1)
    paginator = Paginator(goods, 3)
    curr_page = paginator.page(int(page))
    context = {
        'title': 'Home - каталог',
        'goods': curr_page,
        'slug_url':category_slug,
    }
    return render(request, 'goods/catalog.html', context=context)

def product(request, product_slug, category_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product':product,
    }
    return render(request, 'goods/product.html', context=context)