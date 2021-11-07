from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def cars(request):
    return render(request,'car/cars.html')
    #return HttpResponse('Hello World')
