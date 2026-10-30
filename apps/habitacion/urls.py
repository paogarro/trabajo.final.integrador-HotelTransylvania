from django.urls import path

from .views import HabitacionListView, HabitacionCreateView, HabitacionUpdateView, HabitacionDeleteView

app_name = 'habitacion'

urlpatterns = [
    path('', HabitacionListView.as_view(), name='habitacion_list'),
    path('crear/', HabitacionCreateView.as_view(), name='habitacion_create'),
    path('<int:pk>/editar/', HabitacionUpdateView.as_view(), name='habitacion_update'),
    path('<int:pk>/eliminar/', HabitacionDeleteView.as_view(), name='habitacion_delete'),
]
