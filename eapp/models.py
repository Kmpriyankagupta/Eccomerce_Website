from django.db import models

# Create your models here.
class highlightdata(models.Model):
    image = models.ImageField(upload_to='mainimage')
    image_title = models.CharField(max_length=50)
    image_description = models.CharField(max_length=200)
    
    def __str__(self):
            return self.image_title
    
    
class offer(models.Model):
    special_offer_image = models.ImageField(upload_to='offerimage')
    special_offer_title = models.CharField(max_length=50)
    special_offer_description = models.CharField(max_length=200)
    def __str__(self):
            return self.special_offer_title
    
class Categories(models.Model):
    name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='category',default=None,null=True,blank=True)
    
    def __str__(self):
        return self.name
from django.contrib.postgres.fields import ArrayField   
class Product(models.Model):
    slug = models.CharField(max_length=100, blank=True, null=True, unique=True)
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.BigIntegerField(default=0)
    price_caption = models.CharField(max_length=10)
    rateing = models.FloatField(default=2)
    image = models.ImageField(upload_to='product_image',default=None,null=True,blank=True)
    deal_price = models.BigIntegerField(default=10000)
    sizes = ArrayField(
        models.CharField(max_length=9),  
        blank=True,
        default=list
    )
    colors = ArrayField(
        models.CharField(max_length=9),  
        blank=True,
        default=list
    )
    sort_des = models.CharField(max_length=100,blank=True, null=True)
    long_des = models.CharField(max_length=500,blank=True, null=True)
    # quantity = models.IntegerField(default=0)
    
    def __str__(self):
            return self.product_name
        
class Reviews(models.Model):
    rating = models.FloatField()
    mgs = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name        
# class Cart(models.Model):
#     product_id = models.ForeignKey("Product",  on_delete=models.CASCADE ,to_field='product_name')
#     cont = 

class register_company(models.Model):
    name = models.CharField(max_length=100, default='name')
    image = models.ImageField(upload_to='company',default=None,null=True,blank=True)
    
    def __str__(self):
        return self.name
    