from django.db import models
from rotiseria.models.rol import Rol

class Usuario (models.Model):
    alias = models.CharField(max_length=50, primary_key=True)
    contrasenia = models.CharField(max_length=12)
    rol= models.ForeignKey(Rol, on_delete=models.CASCADE)