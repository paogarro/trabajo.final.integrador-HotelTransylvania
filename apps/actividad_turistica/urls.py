from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ActividadListView, ActividadCreateView, ActividadUpdateView, ActividadDeleteView

app_name = 'actividad_turistica'

urlpatterns = [
    path('', login_required(ActividadListView.as_view()), name='actividad_turistica_list'),
    path('crear/', login_required(ActividadCreateView.as_view()), name='actividad_turistica_create'),
    path('<int:pk>/editar/', login_required(ActividadUpdateView.as_view()), name='actividad_turistica_update'),
    path('<int:pk>/eliminar/', login_required(ActividadDeleteView.as_view()), name='actividad_turistica_delete'),
]
