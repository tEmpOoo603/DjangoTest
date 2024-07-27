from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from goods.models import Products, Categories


def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all().select_related('category')
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug).select_related('category'))
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