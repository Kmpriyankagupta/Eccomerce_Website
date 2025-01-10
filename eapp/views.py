from django.shortcuts import render
from eapp.models import *
def index(request):
    highlightdata1 = highlightdata.objects.all()
    offers = offer.objects.all()
    categories = Categories.objects.all()
    product = Product.objects.all()
    return render(request, 'eapp/index.html',{'highlightdata1':highlightdata1, 'offers':offers, 'categories':categories, 'product':product})
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
