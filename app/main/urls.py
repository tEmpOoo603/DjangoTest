from django.urls import path
from main import views as main

app_name = 'main'

urlpatterns = [
    path('', main.IndexView.as_view(), name='index'),
    path('about/', main.AboutView.as_view(), name='about'),
]