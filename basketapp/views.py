from django.shortcuts import render


def main(requset):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(requset, 'basketapp/basket.html', context)