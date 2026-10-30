from django.db import models

# Create your models here.
    
class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

