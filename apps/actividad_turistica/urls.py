from django.urls import path

from .views import ActividadListView, ActividadCreateView, ActividadUpdateView, ActividadDeleteView

app_name = 'actividad_turistica'

urlpatterns = [
    path('', ActividadListView.as_view(), name='actividad_turistica_list'),
    path('crear/', ActividadCreateView.as_view(), name='actividad_turistica_create'),
    path('<int:pk>/editar/', ActividadUpdateView.as_view(), name='actividad_turistica_update'),
    path('<int:pk>/eliminar/', ActividadDeleteView.as_view(), name='actividad_turistica_delete'),
]
