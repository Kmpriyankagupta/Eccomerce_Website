from django.shortcuts import render
from django.http import JsonResponse
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
from django.shortcuts import render, get_object_or_404
def detail(request,slug):
    details = get_object_or_404(Product, slug=slug)
    related_product = Product.objects.filter(category=details.category)
    # print('kkhhgg',related_product.reviewc)
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        email = request.POST.get('email')
        yourreview = request.POST.get('yourreview')
        review = Reviews.objects.create(
            productid = details,
            name=name,
            rating=rating,
            mgs=yourreview,
            email =email,
        )
        review.save()
    review_count = Reviews.objects.filter(productid=details).count()
    reviews = Reviews.objects.filter(productid=details)
    # print('jdfbjhdbf', )
    return render(request, 'eapp/detail.html',{'details':details,'reviews':reviews, 'review_count':review_count,'related_product':related_product})
def cart(request):
    return render(request, 'eapp/cart.html')
def checkout(request):
    return render(request, 'eapp/checkout.html')
def contact(request):
    return render(request, 'eapp/contact.html')

def get_product_data(request):
    products = Product.objects.all().values(
        'id', 'category__name', 'product_name', 'price', 'price_caption', 'rateing', 'image', 'deal_price',
    'slug')
    product_list = list(products)
    return JsonResponse({'products': product_list})
