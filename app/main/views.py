from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home_Made'
        context['content'] = 'Магазин мебели HOME_MADE'
        return context


# def index(request):
#     user_info = {
#         'title': 'Home_Made',
#         'content': 'Магазин мебели HOME_MADE',
#     }
#     return render(request, 'main/index.html', context=user_info)


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        context['content'] = 'Здесь вы найдётся информацию о нас!'
        context['text_on_page'] = 'Дополнительная информация о нашем магазине и товарах'
        return context
# def about(request):
#     data = {
#         'title': 'О нас',
#         'content': 'Здесь вы найдётся информацию о нас!',
#         'text_on_page': 'Дополнительная информация о нашем магазине и товарах',
#     }
#     return render(request, 'main/about.html', context=data)
