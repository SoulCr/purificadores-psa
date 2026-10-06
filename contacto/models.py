from django.db import models


class Consulta(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField('teléfono', max_length=30, blank=True)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    atendida = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'consulta'
        verbose_name_plural = 'consultas'

    def __str__(self):
        return f'{self.nombre} - {self.fecha:%d/%m/%Y}'