from django.db import models
from rotiseria.models.usuario import Usuario

class Bloque(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)     