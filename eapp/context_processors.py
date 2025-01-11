from .models import *

def my_model_processor(request):
    data = Categories.objects.all()  # Assuming you want the first object
    return {'my_model_data': data}