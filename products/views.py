from django.shortcuts import render, HttpResponse
from .models import Product, ProductCategory


def index(request):
    return HttpResponse(Product.objects.all())