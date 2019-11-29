from django.db import models

class EstadoPedido (models.Model):
    estado = models.CharField(max_length=40)
    # pendiente: listo para aceptar o rechazar
    # cancelado: es cuando el recepcionita lo rechaza
    # confirmado: cuando el recepcionista lo acepta
    

    def __str__(self):
        return str(self.estado)