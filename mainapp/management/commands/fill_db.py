from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser
import csv


class Command(BaseCommand):

    def import_data(self, csv_content, action):
        if action == 'categories':
            ProductCategory.objects.all().delete()
            for row in csv_content:
                category = row.get('category')
                ProductCategory.upload_to_db(self, category)

        if action == 'products':
            Product.objects.all().delete()
            for row in csv_content:
                products = row.values()
                Product.upload_to_db(self, list(products))

    def csv_reader(self, file):
        reader = csv.DictReader(file, delimiter=',')
        return reader

    def handle(self, *args, **options):
        filename = 'price.csv'
        with open(filename, 'r', encoding='utf-8') as csv_file:
            csv_content = self.csv_reader(csv_file)
            self.import_data(csv_content, 'categories')

        with open(filename, 'r', encoding='utf-8') as csv_file:
            csv_content = self.csv_reader(csv_file)
            self.import_data(csv_content, 'products')

        super_user = ShopUser.objects.create_superuser(username='django',
                                                       email='django@art-laser.com.ua',
                                                       password='geekbrains',
                                                       age=35
                                                       )