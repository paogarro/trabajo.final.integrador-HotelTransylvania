from django.db import models
from django.core.exceptions import ValidationError

from apps.habitacion.models import Habitacion
from apps.cliente.models import Cliente
from apps.actividad_turistica.models import ActividadTuristica
# Create your models here.


class Reserva(models.Model):                    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='reservas')
    actividad_turistica = models.ManyToManyField(ActividadTuristica, related_name='reservas', blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    @property

    def total_reserva(self):
        total_habitacion = self.habitacion.precio * (self.fecha_fin - self.fecha_inicio).days
        total_actividades = sum(actividad.precio for actividad in self.actividad_turistica.all())
        return total_habitacion + total_actividades
    def clean(self):
        super().clean()
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_inicio >= self.fecha_fin:
                raise ValidationError("La fecha de inicio no puede ser mayor que la fecha de fin.")
            solapadas = Reserva.objects.filter(habitacion=self.habitacion).exclude(id=self.id).filter(
                fecha_inicio__lt=self.fecha_fin,
                fecha_fin__gt=self.fecha_inicio
            )
            if solapadas.exists():
                raise ValidationError("Ya existe una reserva para esta habitación en las fechas seleccionadas.")

    def __str__(self):
        return f'Reserva de {self.cliente} - Habitación {self.habitacion.numero}'
