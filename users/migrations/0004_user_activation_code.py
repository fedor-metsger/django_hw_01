# Generated by Django 4.2.1 on 2023-06-21 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
