from django.db import models
from rotiseria.Models.usuario import Usuario

class Repartidor (Usuario, models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)