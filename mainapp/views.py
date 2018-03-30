from django.shortcuts import render
import json
import os
from mainapp.models import ProductCategory, Product

def main(request):
    title = 'Главная'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        'title': title,
        'categories': categories,
        'products': products[:4],
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    title = 'Каталог'
    categories = []
    products = []
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
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    """ Загрузка данных из json файла на диске """
    dirname = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(dirname, 'contact_data.json')
    with open(filename, 'r', encoding='utf-8') as file:
        locations = json.load(file)

    title = 'Контакты'
    context = {
        'title': title,
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)
