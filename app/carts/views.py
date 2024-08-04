from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def cart_add(request):
    pass
def cart_remove(request):
    return HttpResponseRedirect(reverse('main:index'))
def cart_change(request):
    pass