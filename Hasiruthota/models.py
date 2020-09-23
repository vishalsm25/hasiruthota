from django.db import models

# Create your models here.
class featured_product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price1 = models.IntegerField()
    price2 = models.IntegerField()

class new_product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price1 = models.IntegerField()
    price2 = models.IntegerField()

class best_plants(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price1 = models.IntegerField()
