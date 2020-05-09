from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from django.core import serializers
from multiprocessing import Process
import datetime, time, json
from django.http import HttpResponse
# Create your views here.


def Get_All_Products(request):
    products = Product.objects.all()
    prod_list = serializers.serialize('json', products)
    return HttpResponse(prod_list, content_type="text/json-comment-filtered")

def Product_Details(request, name):
    products = Product.objects.filter(name=name)
    prod_list = serializers.serialize('json', products)
    return HttpResponse(prod_list, content_type="text/json-comment-filtered")
