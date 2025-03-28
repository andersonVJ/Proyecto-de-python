from django.db import models
from django.contrib.auth.models import User


class Recurso(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre del Recurso")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    tipo = models.CharField(max_length=100, verbose_name="Tipo de Recurso")
    cantidad_total = models.IntegerField(default=0, verbose_name="Cantidad Total")
    cantidad_disponible = models.IntegerField(default=0, verbose_name="Cantidad Disponible")
    unidad_medida = models.CharField(max_length=50, blank=True, null=True, verbose_name="Unidad de Medida")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    def __str__(self):
        return self.nombre
    

class SolicitudRecurso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario Solicitante")
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE, verbose_name="Recurso Solicitado")
    cantidad_solicitada = models.IntegerField(default=1, verbose_name="Cantidad Solicitada")
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")
    fecha_entrega_esperada = models.DateField(verbose_name="Fecha de Entrega Esperada")
    fecha_devolucion_esperada = models.DateField(null=True, blank=True, verbose_name="Fecha de Devolución Esperada") # Para recursos que se prestan
    fecha_entrega_real = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Entrega Real")
    fecha_devolucion_real = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Devolución Real")
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('aprobada', 'Aprobada'),
            ('rechazada', 'Rechazada'),
            ('entregada', 'Entregada'),
            ('devuelta', 'Devuelta'),
        ],
        default='pendiente',
        verbose_name="Estado de la Solicitud"
    )
    notas = models.TextField(blank=True, null=True, verbose_name="Notas de la Solicitud")

    def __str__(self):
        return f"Solicitud de {self.cantidad_solicitada} {self.recurso.nombre} por {self.usuario.username}"

    class Meta:
        verbose_name = "Solicitud de Recurso"
        verbose_name_plural = "Solicitudes de Recursos"
