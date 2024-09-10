from django.db import models

class Mensaje(models.Model):
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.CharField(max_length=255, default='Sin asunto')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.remitente} -> {self.destinatario}: {self.asunto}'
