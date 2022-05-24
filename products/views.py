from django.shortcuts import render , get_object_or_404
from .models import Product
# Create your views here.


def product(request):
    products = Product.objects
    return render(request , 'products.html' , {'products' : products})


def product_s(request , product_id):
    product = Product.objects
    product_s = get_object_or_404(Product , pk=product_id)
    return render(request, 'product.html' , {'product_s' : product_s, 'products': product})


# def base(request):
#     products = Product.objects
#     return render(request, 'base.html', {'products': products})