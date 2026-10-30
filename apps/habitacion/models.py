from django.db import models

# Create your models here.

class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    hotel = models.ForeignKey('hotel.Hotel', on_delete=models.CASCADE, related_name='habitaciones')

    def __str__(self):
        return f'Habitación {self.numero} - {self.tipo}'

