from django.db import models

# Create your models here.

class Myform(models.Model):
    acidity1 = models.FloatField(default=0)
    quantity1 = models.FloatField(default=0)
    acidity2 = models.FloatField(default=0)
    quantity2 = models.FloatField(default=0)
    acidity3 = models.FloatField(default=0)
    quantity3 = models.FloatField(default=0)
    total = models.FloatField(default=0)
    result = models.FloatField(default=0)

