from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='basket', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    total_price = models.DecimalField(verbose_name='стоимость', max_digits=8, decimal_places=2, default=0)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        # items = Basket.objects.filter(user=self.user)
        items = self.user.basket.all()
        total_quantity = sum(list(map(lambda x: x.quantity, items)))
        return total_quantity

    @property
    def total_cost(self):
        # items = Basket.objects.filter(user=self.user)
        items = self.user.basket.all()
        totalcost = sum(list(map(lambda x: x.product_cost, items)))
        return totalcost

    @staticmethod
    def get_basket(request):
        if request.user.is_authenticated:
            basket = request.user.basket.all()
        else:
            basket = []
        return basket
