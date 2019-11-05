from django.db import models
from rotiseria.models.producto import Producto
from rotiseria.models.bloque import Bloque
from rotiseria.models.cliente import Cliente
from rotiseria.models.estadopedido import EstadoPedido
from datetime import datetime

class Pedido (models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default = datetime.now)
    total = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    productos = models.ManyToManyField(Producto)
    bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estadoPedido= models.ForeignKey(EstadoPedido, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return str(self.id)

    def generarTotal (self, subtotal):
        self.total=+ subtotal

    
