from django.db import models
from rotiseria.models.categoría import Categoría

class Producto(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    descripcion = models.CharField(max_length=50)
    foto = models.ImageField()
    precioActual = models.DecimalField()
    categoria= models.ForeignKey(Categoría, on_delete=models.CASCADE)
    ganancia= models.IntegerField()

    def __str__(self):
        return self.nombre