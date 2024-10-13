from django.shortcuts import render, HttpResponse
from .models import Checkout

import os
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return HttpResponse("This is the about page")
def service(request):
    return HttpResponse("This is the service page")
def buy(request):
    return render(request, 'buy.html')
def shake(request):
    return render(request, 'shake.html')
def pay(request):
    return render(request, 'pay.html')
def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        checkout = Checkout(name=name, email=email, phone=phone)
        checkout.save()
    return render(request, 'checkout.html')

