from django.shortcuts import render, get_list_or_404

from goods.models import Products, Categories


def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all().select_related('category')
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug).select_related('category'))
    context = {
        'title': 'Home - каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context=context)

def product(request, product_slug, category_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product':product,
    }
    return render(request, 'goods/product.html', context=context)