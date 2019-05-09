from django.db import models

class Viðskiptavinur(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=999)
    year_of_start = models.DateTimeField()

