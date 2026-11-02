from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import HabitacionListView, HabitacionCreateView, HabitacionUpdateView, HabitacionDeleteView, HabitacionDetailView

app_name = 'habitacion'

urlpatterns = [
    path('', login_required(HabitacionListView.as_view()), name='habitacion_list'),
    path('crear/', login_required(HabitacionCreateView.as_view()), name='habitacion_create'),
    path('<int:pk>/editar/', login_required(HabitacionUpdateView.as_view()), name='habitacion_update'),
    path('<int:pk>/eliminar/', login_required(HabitacionDeleteView.as_view()), name='habitacion_delete'),
    path('<int:pk>/', login_required(HabitacionDetailView.as_view()), name='habitacion_detail'),
]
