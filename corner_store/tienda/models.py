from django.db import models
from inventario.models import Articulo
# Create your models here.

class Item(models.Model):
    titulo = models.CharField(max_length=50)
    articulos = models.ManyToManyField(Articulo)
