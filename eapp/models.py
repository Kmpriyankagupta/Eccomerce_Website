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
    
class Product(models.Model):
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.BigIntegerField(default=0)
    price_caption = models.CharField(max_length=10)
    rateing = models.FloatField(default=2)
    image = models.ImageField(upload_to='product_image',default=None,null=True,blank=True)
    deal_price = models.BigIntegerField(default=10000)
    
    def __str__(self):
            return self.product_name
        
# class Cart(models.Model):
#     product_id = models.ForeignKey("Product",  on_delete=models.CASCADE ,to_field='product_name')
#     cont = 

class register_company(models.Model):
    name = models.CharField(max_length=100, default='name')
    image = models.ImageField(upload_to='company',default=None,null=True,blank=True)
    
    def __str__(self):
        return self.name
    