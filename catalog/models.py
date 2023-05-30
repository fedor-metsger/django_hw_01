
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    # created_at = models.DateField(verbose_name='дата создания', null=True, blank=True)

    def __str__(self):
        # return f'Category({self.name})'
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    photo = models.ImageField(verbose_name='изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name='цена')
    creation_date = models.DateField(verbose_name='дата создания')
    modification_date = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'Product({self.name})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    phone = models.CharField(max_length=20, verbose_name='телефон')
    email = models.CharField(max_length=50, verbose_name='e-mail')


    def __str__(self):
        return f'Contact({self.name})'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

