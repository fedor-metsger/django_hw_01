
from django.conf import settings
from django.core.cache import cache

from catalog.models import Category

def get_cached_categories(cat_id):
    if settings.LOW_CACHED:
        key = f'categories_list_{cat_id}'
        cat_list = cache.get(key)
        if cat_list is None:
            cat_list = Category.objects.filter(pk=cat_id)
            cache.set(key, cat_list)
    else:
        cat_list = Category.objects.filter(pk=cat_id)

    return cat_list