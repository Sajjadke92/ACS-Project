from django.db import models
from datetime import date

class Drinks_Inventory(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Items(models.Model):
    Drinks_Inventory = models.ForeignKey(Drinks_Inventory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiry = models.DateField(default=date.today)
    description = models.TextField(blank=True)


