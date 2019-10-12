from django.db import models
from rotiseria.models.producto import Producto
from rotiseria.models.bloque import Bloque
from rotiseria.models.cliente import Cliente
from rotiseria.models.estadopedido import Estadopedido

class Pedido (models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    productos = models.ManyToManyField(Producto)
    bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estadoPedido= models.ForeignKey(Estadopedido, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def generarTotal (self, subtotal):
        self.total=+ subtotal