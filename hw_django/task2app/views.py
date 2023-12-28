from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def order(request):
    return HttpResponse('На этой странице будут отображаться заказы.')
