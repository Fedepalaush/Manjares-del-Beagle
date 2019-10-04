from django.db import models
from rotiseria.models.usuario import Usuario

class Repartidor (Usuario, models.Model):
    def __str__(self):
        return super.alias