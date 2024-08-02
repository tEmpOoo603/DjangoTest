from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm


def login(request):
    if request.POST:
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Страница авторизации',
        'form': form,
    }
    return render(request, 'users/login.html', context=context)

def registration(request):
    context = {
        'title':'Страница регистрации'
    }
    return render(request, 'users/registration.html', context=context)

def profile(request):
    context = {
        'title':'Страница профиля'
    }
    return render(request, 'users/profile.html', context=context)

def logout(request):
    context = {
        'title':'Страница выхода с аккаунта'
    }
    return render(request, 'users/anything.htmlusers/', context=context)

