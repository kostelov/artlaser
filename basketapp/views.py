from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket


def main(requset):
    title = 'Корзина'
    context = {
        'title': title,
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
