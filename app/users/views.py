from django.shortcuts import render

def login(request):
    context = {
        'title':'Страница авторизации'
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

