from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from mainapp.models import Product
from basketapp.models import Basket


@login_required
def main_basket(requset):
    title = 'Корзина'
    basket, count_product, total = Basket.get_basket(requset)
    context = {
        'title': title,
        'basket': basket,
        'count_product': count_product,
        'total': total,
    }
    return render(requset, 'basketapp/basket.html', context)


@login_required
def product_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))
    product = get_object_or_404(Product, pk=pk)
    basket_object = Basket.objects.filter(user=request.user, product=product).first()
    if basket_object:
        basket_object.quantity += 1
        basket_object.total_price += basket_object.product.price
        basket_object.save()
    else:
        Basket.objects.create(user=request.user, product=product, total_price=product.price, quantity=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def product_del(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
