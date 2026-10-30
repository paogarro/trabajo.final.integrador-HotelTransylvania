from django.contrib import admin

# Register your models here.
from apps.habitacion.models import Habitacion

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'precio')
    search_fields = ('numero', 'tipo')
    list_filter = ('tipo', 'precio')