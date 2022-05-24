from django.shortcuts import render
from products.models import Product
from hero.models import Hero

products = Product.objects


def homepage(request):
    hero = Hero.objects
    return render(request, 'home.html' , {'products': products, 'hero': hero})


def base(request):
    return render(request, 'base.html', {'products': products})


def hakkimizda(request):
    return render(request, 'hakkimizda.html', {'products': products})


def iletisim(request):
    return render(request, 'iletisim.html', {'products': products})