from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from mainapp.models import Product
from basketapp.models import Basket


@login_required
def main_basket(requset):
    title = 'Корзина'
    basket = Basket.get_basket(requset)
    context = {
        'title': title,
        'basket': basket,
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

@login_required
def product_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.filter(pk=int(pk)).first()

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket = request.user.basket.all()
            # .order_by('product__category')

        context = {
            'basket': basket,
        }
        result = render_to_string('basketapp/includes/inc__basket_list.html', context)

        return JsonResponse({'result': result})
