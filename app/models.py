from django.db import models

# Create your models here.
class Math(models.Model):
    add = models.CharField(max_length=50, blank=False)
    substract = models.CharField(max_length=50, blank=False)
    multiply = models.CharField(max_length=50, blank=False)
    devide = models.CharField(max_length=50, blank=False)
