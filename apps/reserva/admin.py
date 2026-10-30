from django.contrib import admin

from apps.reserva.models import Reserva

# Register your models here.

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'habitacion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('cliente__nombre', 'habitacion__numero', 'actividad_turistica__nombre')
    list_filter = ('fecha_inicio', 'fecha_fin')