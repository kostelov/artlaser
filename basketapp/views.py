from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket


def main_basket(requset):
    title = 'Корзина'
    count_product = 0
    total = 0
    basket = Basket.get_basket(requset)
    for item in basket:
        count_product += int(item.quantity)
        total += int(item.product.price) * item.quantity
    context = {
        'title': title,
        'basket': basket,
        'count_product': count_product,
        'total': total,
    }
    return render(requset, 'basketapp/basket.html', context)


def product_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_object = Basket.objects.filter(user=request.user, product=product).first()
    if basket_object:
        basket_object.quantity += 1
        basket_object.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
