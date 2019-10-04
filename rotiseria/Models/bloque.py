from django.db import models
from rotiseria.Models.repartidor import Repartidor

class Bloque(models.Model):
    id=models.IntegerField()
    fecha= models.DateField()
    repartidor= models.ForeignKey(Repartidor)

    def __str__(self):
        return self.id