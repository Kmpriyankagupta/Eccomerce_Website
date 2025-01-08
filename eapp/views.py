from django.shortcuts import render

def index(request):
    return render(request, 'eapp/index.html')
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
