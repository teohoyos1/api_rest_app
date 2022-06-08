from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2, default=1)
    quantity = models.IntegerField(default=0)