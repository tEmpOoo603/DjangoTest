from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    user_info = {
        'is_authenticated':False,
        'name':'Efim',
        'pass':'123',
        'cars':['BMW','AUDI','MERCEDES'],
        'parents':{'mom':'Tatiana'},
    }
    return render(request, 'main/index.html', context=user_info)
def about(request):
    data = {
        'title':'О нас',
        'content':'Здесь вы найдётся информацию о нас!',
    }
    return render(request, 'main/about.html', context=data)
