from django.shortcuts import render

from .models import Product
from .forms import ProductForm

# Create your views here.

def product_create_view(request):
    form = ProductForm(request.Post or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    prod = Product.objects.get(id=1)
    # context = {
    #     'title': prod.title,
    #     'description': prod.description,
    #     'price': prod.price,
    #     'summary': prod.summary,
    # }

    context = {
        'obj': prod
    }
    return render(request, "products/product_detail.html", context)