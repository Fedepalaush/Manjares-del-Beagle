from django.db import models
from rotiseria.Models.producto import Producto
from rotiseria.Models.bloque import Bloque
from rotiseria.Models.cliente import Cliente

class Pedido (models.Model):
    id= models.IntegerField(primary_key=True)
    fecha= models.DateField()
    hora=models.TimeField
    total= models.DecimalField()
    productos= models.ManyToManyField(Producto)
    bloque= models.ForeignKey(Bloque)
    cliente=models.ForeignKey(Cliente)

    def __str__(self):
        return self.id