from django.db import models
from rotiseria.models.repartidor import Repartidor

class Bloque(models.Model):
    id=models.IntegerField()
    fecha= models.DateField()
    repartidor= models.ForeignKey(Repartidor, on_delete=models.CASCADE)

    def __str__(self):
        return self.id