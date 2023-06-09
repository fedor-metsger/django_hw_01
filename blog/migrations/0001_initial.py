# Generated by Django 4.2.1 on 2023-05-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('content', models.TextField(verbose_name='cодержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('creation_date', models.DateField(verbose_name='дата создания')),
                ('published', models.BooleanField(verbose_name='признак публикации')),
                ('views', models.IntegerField(verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
            },
        ),
    ]
