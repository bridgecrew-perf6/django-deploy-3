from django.shortcuts import render
from .models import Gallery
from products.models import Product
# Create your views here.


def gallery(request):
    gallery = Gallery.objects
    products = Product.objects
    return render(request, 'gallery.html', {'gallery': gallery, 'products': products})