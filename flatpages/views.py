from django.shortcuts import render
from django.http import HttpResponse
from django import template
def home(request):
    return render(request, 'static_handler.html')
# Create your views here.
