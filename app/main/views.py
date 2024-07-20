from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    user_info = {
        'title': 'Home_Made',
        'content': 'Магазин мебели HOME_MADE',
    }
    return render(request, 'main/index.html', context=user_info)


def about(request):
    data = {
        'title': 'О нас',
        'content': 'Здесь вы найдётся информацию о нас!',
        'text_on_page': 'Дополнительная информация о нашем магазине и товарах',
    }
    return render(request, 'main/about.html', context=data)
