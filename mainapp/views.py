import json
import os
import random
from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket


def get_categories():
    categories = []
    all_categories = {
        'pk': 0,
        'name': 'все'
    }

    categories.append(all_categories)
    categories.extend(ProductCategory.objects.all())

    return categories

def main(request):
    title = 'Главная'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    basket, count_product, total_price = Basket.get_basket(request)
    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)
    context = {
        'title': title,
        'categories': categories,
        'products': products[:4],
        'count_product': count_product,
        'basket': basket,
        'same_products': same_products,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    title = 'Каталог'
    products = []
    basket, count_product, total_price = Basket.get_basket(request)
    categories = get_categories()

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

    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)

    context = {
        'title': title,
        'categories': categories,
        'products': products,
        'count_product': count_product,
        'basket': basket,
        'hot_product': hot_product,
        'same_products': same_products,
        'hot': True,
    }
    return render(request, 'mainapp/product_detail.html', context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = get_categories()
    basket, count_product, total_price = Basket.get_basket(request)
    same_products = get_same_product(product)
    title = product.name

    context = {
        'title': title,
        'categories': categories,
        'hot_product': product,
        'basket': basket,
        'count_product': count_product,
        'same_products': same_products,
        'hot': False,
    }

    return render(request, 'mainapp/product_detail.html', context)



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


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_product(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:4]
    return same_products
