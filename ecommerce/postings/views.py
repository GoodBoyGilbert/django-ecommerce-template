from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def detail(request, product_id):
    # Fetch the product based on the product_id
    product = get_object_or_404(Product, pk=product_id)
    
    # Fetch the newest products for the related section
    newest_products = Product.objects.order_by('-id')[:4]

    return render(request, "detail.html", {'product': product, 'newest_products': newest_products})

def about(request):
    products = Product.objects.all()
    return render(request,"about.html", {'products': products})