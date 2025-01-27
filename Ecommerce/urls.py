
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from eapp.views import *
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('shop/',shop),
    path('detail/<slug:slug>/', detail, name='detail'),
    path('cart/', cart),
    path('checkout/', checkout),
    path('contact/', contact),
    path('productapi/',get_product_data),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
