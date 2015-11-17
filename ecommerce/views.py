from django.shortcuts import render

# Create your views here.
from ecommerce.models import Product


def index(request):
    product_list = Product.objects.all()

    context = {
        'product_list': product_list
    }

    return render(request, 'ecommerce/index.html', context)

def detail(request, id):
    product_detail = Product.objects.get(pk=id)

    context = {
        'product_detail': product_detail
    }

    return render(request, 'ecommerce/detail.html', context)
