from django.shortcuts import render
import json
import os
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket


def main(request):
    title = 'Главная'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    basket, count_product, total_price = Basket.get_basket(request)
    context = {
        'title': title,
        'categories': categories,
        'products': products[:4],
        'count_product': count_product,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    title = 'Каталог'
    categories = []
    products = []
    basket, count_product, total_price = Basket.get_basket(request)
    all_categories = {
        'pk': 0,
        'name': 'все'
    }

    categories.append(all_categories)
    categories.extend(ProductCategory.objects.all())

    if pk:
        pk = int(pk)
        if pk == 0:
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category__pk=pk)

    context = {
        'title': title,
        'categories': categories,
        'products': products,
        'count_product': count_product,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    """ Загрузка данных из json файла на диске """
    dirname = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(dirname, 'contact_data.json')
    with open(filename, 'r', encoding='utf-8') as file:
        locations = json.load(file)

    title = 'Контакты'
    basket, count_product, total_price = Basket.get_basket(request)
    context = {
        'title': title,
        'locations': locations,
        'count_product': count_product,
        'basket': basket,
    }
    return render(request, 'mainapp/contact.html', context)
