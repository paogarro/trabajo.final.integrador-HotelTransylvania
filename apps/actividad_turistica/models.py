from django.db import models


# Create your models here.

class ActividadTuristica(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hotel = models.ForeignKey('hotel.Hotel', on_delete=models.CASCADE, related_name='actividades_turisticas')

    def __str__(self):
        return self.nombre


