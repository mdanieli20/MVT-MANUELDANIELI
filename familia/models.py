from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    anio_nacimiento = models.DateField(null=True)
