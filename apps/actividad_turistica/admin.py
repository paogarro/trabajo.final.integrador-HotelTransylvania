from django.contrib import admin

from apps.actividad_turistica.models import ActividadTuristica
# Register your models here.

@admin.register(ActividadTuristica)
class ActividadTuristicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('nombre',)