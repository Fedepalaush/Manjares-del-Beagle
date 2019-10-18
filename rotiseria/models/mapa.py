from django.db import models
from rotiseria.models.cliente import Cliente

class Mapa(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    latitud = models.CharField(max_length=50, null=True)
    longitud = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.latitud
    

