# Generated by Django 3.1 on 2020-09-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hasiruthota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured_product',
            name='price1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='featured_product',
            name='price2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
