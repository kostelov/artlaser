from django.shortcuts import render


# Create your views here.

def main(request):
    title = 'Главная'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    title = 'Каталог'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    title = 'Контакты'
    locations = [
        {
            'map': 'https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2525.797238591331!2d25.330129232289313!3d50.72370072838036!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!2sua!4v1521399079914',
            'country': 'Украина',
            'phone': '+380 (96) 890-77-11',
            'email': 'office&@art-laser.com.ua',
            'address': 'Рованцы',
            },
        {
            'map': 'https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2122.489204755704!2d25.35729590891547!3d50.755563921938034!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!2sua!4v1521399361082',
            'country': 'Украина',
            'phone': '+380 (95) 908-77-55',
            'email': 'office&@art-laser.com.ua',
            'address': 'г. Луцк, ул. Сухомлинского, 1',
            },
        {
            'map': 'https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2122.3178619805512!2d25.352685748786712!3d50.75934212624163!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!2sua!4v1521399610372',
            'country': 'Украина',
            'phone': '+380 (98) 832-70-60',
            'email': 'office&@art-laser.com.ua',
            'address': 'г. Луцк, ул. Конякина, 1',
            },
    ]
    context = {
        'title': title,
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)
