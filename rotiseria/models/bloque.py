from django.db import models
from rotiseria.models.usuario import Usuario
from datetime import datetime

class Bloque(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default = datetime.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)     