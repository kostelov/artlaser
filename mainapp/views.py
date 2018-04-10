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
    categories.extend(ProductCategory.objects.filter(is_active=True))

    return categories

def main(request):
    title = 'Главная'
    categories = ProductCategory.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True, category__is_active=True)
    basket = Basket.get_basket(request)
    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)
    context = {
        'title': title,
        'categories': categories,
        'products': products[1:5],
        'basket': basket,
        'same_products': same_products,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    title = 'Каталог'
    products = []
    basket = Basket.get_basket(request)
    categories = get_categories()

    if pk:
        pk = int(pk)
        if pk == 0:
            products = Product.objects.filter(category__is_active=True, is_active=True)
        else:
            products = Product.objects.filter(category__pk=pk, is_active=True)

        context = {
            'title': title,
            'categories': categories,
            'products': products,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', context)

    hot_product = get_hot_product()
    same_products = get_same_product(hot_product)

    context = {
        'title': title,
        'categories': categories,
        'products': products,
        'basket': basket,
        'hot_product': hot_product,
        'same_products': same_products,
        'hot': True,
    }
    return render(request, 'mainapp/product_detail.html', context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = get_categories()
    basket = Basket.get_basket(request)
    same_products = get_same_product(product)
    title = product.name

    context = {
        'title': title,
        'categories': categories,
        'hot_product': product,
        'basket': basket,
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
    basket = Basket.get_basket(request)
    context = {
        'title': title,
        'locations': locations,
        'basket': basket,
    }
    return render(request, 'mainapp/contact.html', context)


def get_hot_product():
    products = Product.objects.filter(category__is_active=True)
    return random.sample(list(products), 1)[0]


def get_same_product(hot_product):
    same_products = Product.objects.filter(is_active=True, category=hot_product.category).exclude(pk=hot_product.pk)[:4]
    return same_products
