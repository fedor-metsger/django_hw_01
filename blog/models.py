
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.SlugField(max_length=200, verbose_name='slug')
    content = models.TextField(verbose_name='cодержимое')
    preview = models.ImageField(verbose_name='превью', null=True, blank=True)
    creation_date = models.DateField(verbose_name='дата создания')
    published = models.BooleanField(verbose_name='признак публикации')
    views = models.IntegerField(verbose_name='количество просмотров')

    def __str__(self):
        return f'Article({self.title})'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
