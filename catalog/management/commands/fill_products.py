
# catalog/management/commands/fill_category.py
from django.core.management import BaseCommand

from catalog.models import Category, Contact, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {"id": 1, "name": "Кефир 3%", "description": "Калорийность кефира 3,2%", "category_id": 1,
             "photo": "kefir.webp", "price": 100, "creation_date": "2023-05-26", "modification_date": "2023-05-26"},
            {"id": 2, "name": "Молоко 3%", "description": "Состав: молоко цельное, молоко обезжиренное.", "category_id": 1,
             "photo": "milk.webp", "price": 80, "creation_date": "2023-05-26", "modification_date": "2023-05-26"},
            {"id": 3, "name": "Молоко рисовое натуральное",
             "description": "Калорийность натурального рисового молока составляет 60 ккал на 100 грамм продукта.",
             "category_id": 1,
             "photo": "milk-rice.jpg", "price": 120, "creation_date": "2023-05-26", "modification_date": "2023-05-26"},
            {"id": 4, "name": "Молоко сгущённое с сахаром",
             "description": "Молоко сгущённое с сахаром может иметь разную жирность или быть обезжиренным",
             "category_id": 1,
             "photo": "sguha.jpg", "price": 200, "creation_date": "2023-05-26", "modification_date": "2023-05-26"},
            {"id": 5, "name": "Молоко соевое",
             "description": "Калорийность соевого молока составляет 54 ккал на 100 грамм продукта.", "category_id": 1,
             "photo": "milk-soya.jpg", "price": 150, "creation_date": "2023-05-26", "modification_date": "2023-05-26"},
            {"id": 6, "name": "Молоко сухое цельное",
             "description": "Сухое цельное молоко - широко известный пищевой продукт", "category_id": 1,
             "photo": "milk-dry.jpg", "price": 300, "creation_date": "2023-05-26", "modification_date": "2023-05-26"}
        ]

        Product.objects.all().delete()

        for pr in product_list:
            Product.objects.create(**pr)