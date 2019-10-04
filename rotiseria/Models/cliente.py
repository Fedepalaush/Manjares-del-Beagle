from django.db import models

class Cliente(models.Model):
    dni= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=50)
    telefono= models.IntegerField()
    direccion=models.CharField()

    def __str__(self):
        return self.nombre