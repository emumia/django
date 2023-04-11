from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course(request):
    return HttpResponse("<h1>Assalamualikum, This is Muhammad Imran </br> I'm from Dhaka, Bangladesh</h1>")                       
