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