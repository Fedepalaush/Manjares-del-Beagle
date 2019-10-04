from django.db import models

class Categoría (models.Model):
    nombre= models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.nombre