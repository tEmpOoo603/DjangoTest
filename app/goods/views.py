from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from django.views.generic import DetailView

from goods.models import Products, Categories
from goods.utils import q_search


def catalog(request, category_slug=None):
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    if category_slug == 'all':
        goods = Products.objects.all().select_related('category')
    elif query:
        goods = q_search(query)
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
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context=context)


class ProductView(DetailView):
    template_name = 'goods/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context

# def product(request, product_slug, category_slug):
#     product = Products.objects.get(slug=product_slug)
#     context = {
#         'product':product,
#     }
#     return render(request, 'goods/product.html', context=context)