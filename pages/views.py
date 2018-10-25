from django.shortcuts import render

from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('hello harrison')

# Create your views here.
