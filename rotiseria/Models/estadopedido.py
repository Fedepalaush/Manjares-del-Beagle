from django.db import models

class Estadopedido (models.Model):
    estado= models.IntegerField()  # 1 pendiente  2: en proceso   3: listo


