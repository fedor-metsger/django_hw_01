
# catalog/management/commands/fill_category.py
from django.core.management import BaseCommand

from catalog.models import Category

class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {"id": 1, "name": "Продукты", "description": "Продукты"},
            {"id": 2, "name": "Электроника", "description": "Электроника"},
            {"id": 3, "name": "Одежда", "description": "Одежда"}
        ]

        for cat in category_list:
            Category.objects.create(**cat)