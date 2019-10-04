from django.db import models

class Usuario (models.Model):
    alias = models.CharField(max_length=50, primary_key=True)
    contraseña = models.CharField(max_length=12)
