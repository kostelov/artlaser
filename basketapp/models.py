from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    total_price = models.DecimalField(verbose_name='стоимость', max_digits=8, decimal_places=2, default=0)

    @staticmethod
    def get_basket(request):
        count_product = 0
        total = 0
        if request.user.is_authenticated:
            basket = Basket.objects.filter(user=request.user)
            for item in basket:
                count_product += int(item.quantity)
                total += int(item.total_price)
        else:
            basket = []
        return basket, count_product, total
