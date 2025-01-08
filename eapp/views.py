from django.shortcuts import render
from eapp.models import *
def index(request):
    highlightdata1 = highlightdata.objects.all()
    for i in highlightdata1:
        print(i.image)
    print(highlightdata1[0].image)
    return render(request, 'eapp/index.html',{'highlightdata1':highlightdata1})
def shop(request):
    return render(request,'eapp/shop.html')
def detail(request):
    return render(request, 'eapp/detail.html')
def cart(request):
    return render(request, 'eapp/cart.html')
def checkout(request):
    return render(request, 'eapp/checkout.html')
def contact(request):
    return render(request, 'eapp/contact.html')
