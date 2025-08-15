from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

months = {}
def index(request):
    return HttpResponse("This Works!")

def feb(request):
    return HttpResponse("This is Feb challenge")