from django.db import models

class Categoría (models.Model):
    nombre= models.CharField(max_length=50)