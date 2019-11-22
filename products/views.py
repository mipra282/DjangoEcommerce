from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Product
from django.core import serializers

# Create your views here.


def products_view(request):
    products = Product.objects.all()
    content = {
       'products':products
    }
    #Product1 = Product.objects.get(id=1)
    #Product2 = Product.objects.get(id=2)
    #content = {
        #"Product1":Product1,
        #"Product2":Product2
   # }
   
    print(content)
    return render(request,'products.html',content)

# def products_view(request):
#     products = Product.objects.all()
#
#     products_json = serializers.serialize('json',products)
#
#     return HttpResponse(products_json, content_type='application/json')