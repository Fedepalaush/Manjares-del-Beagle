from django.db import models
from rotiseria.models.producto import Producto
from rotiseria.models.bloque import Bloque
from rotiseria.models.cliente import Cliente

class Pedido (models.Model):
    id= models.IntegerField(primary_key=True)
    fecha= models.DateField()
    hora=models.TimeField
    total= models.DecimalField()
    productos= models.ManyToManyField(Producto,on_delete=models.CASCADE)
    bloque= models.ForeignKey(Bloque,on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)

    def __str__(self):
        return self.id