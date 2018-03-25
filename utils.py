import csv
import os
import sys
import django


def add_product(row, cats):
    product = Product()
    try:
        product.category = cats
        product.name = row[1]
        product.vendor_id = row[2]
        product.image = row[3]
        product.short_descript = row[4]
        product.description = row[5]
        product.price = row[6]
        product.quantity = row[7]
        product.save()
    except Exception as e:
        print(e)


def import_data(filename):
    categories = ProductCategory.objects.all()
    category_list = [str(_) for _ in categories]
    with open(filename, 'r', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for cats in categories:
            for row in data:
                if row[0] != 'category':
                    if row[0] not in category_list:
                        categorys = ProductCategory()
                        categorys.name = row[0]
                        categorys.save()
                        add_product(row, cats)
                    else:
                        add_product(row, cats)


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Указываем путь до папки проекта Django в котором находится файл settings.py
    project_dir = os.path.join(current_dir, 'artlaser')
    # Добавляем в переменную sys.path путь до проекта Django
    sys.path.append(project_dir)
    # Определяем переменную с настройками Django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    # Загружаем настройки Django
    django.setup()

    from mainapp.models import ProductCategory, Product

    file = os.path.join(current_dir, 'price.csv')
    import_data(file)
