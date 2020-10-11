from django.shortcuts import render

from .models import Product
# Create your views here.
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