from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=120)
    cantidad = models.IntegerField()
    pais = models.CharField(max_length=120)

