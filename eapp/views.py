from django.shortcuts import render

from django.db.models import Count
from eapp.models import *
def index(request):
    highlightdata1 = highlightdata.objects.all()
    offers = offer.objects.all()
    categories = Categories.objects.all()
    product = Product.objects.all()
    compnay = register_company.objects.all()
    category_product_count = Product.objects.values('category__id', 'category__name').annotate(product_count=Count('id'))
    for i in category_product_count:
        print(i['product_count'])
    print('dfjkhi',category_product_count)
    return render(request, 'eapp/index.html',{'highlightdata1':highlightdata1, 'offers':offers, 'categories':categories, 'product':product, 'compnay' :compnay,'category_product_count':category_product_count})
def shop(request):
    product = Product.objects.all()
    return render(request,'eapp/shop.html',{'product':product})
def detail(request):
    return render(request, 'eapp/detail.html')
def cart(request):
    return render(request, 'eapp/cart.html')
def checkout(request):
    return render(request, 'eapp/checkout.html')
def contact(request):
    return render(request, 'eapp/contact.html')
