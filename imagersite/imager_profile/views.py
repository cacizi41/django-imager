from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render('Hello Django')

# Create your views here.
