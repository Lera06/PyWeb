

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from datetime import datetime
from random import random


# Create your views here.
class CurrentDateView(View):

    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)


class RandomNumberView(View):

    def get(self, request):
        html = f"{random()}"
        return HttpResponse(html)


class HelloWorldView(View):

    def get(self, request):
        html = "<h1>Hello, World</h1>"
        return HttpResponse(html)


class IndexView(View):
    def get(self, request):
        return render(request, 'other/index.html')
