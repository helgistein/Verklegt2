from django.db import models

from viðskiptavinur.models import Viðskiptavinur


class Housecategory(models.Model):
    name = models.CharField(max_length=255)

class House(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(Housecategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    viðskiptavinur = models.ForeignKey(Viðskiptavinur, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class HouseImage(models.Model):
    image = models.CharField(max_length=999)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    def __str__(self):
        return self.image