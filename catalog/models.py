from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    # created_at = models.DateField(verbose_name='дата создания', null=True, blank=True)

    def __str__(self):
        return f'Category({self.name})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name='цена')
    creation_date = models.DateField(verbose_name='дата создания')
    modification_date = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'Product({self.name})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'