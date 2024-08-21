from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    return render(request, 'main/index.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'main/product_detail.html', context)
