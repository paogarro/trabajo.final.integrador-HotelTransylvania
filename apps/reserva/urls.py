from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ReservaListView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView, ReservaDetailView

app_name = 'reserva'

urlpatterns = [
    path('', login_required(ReservaListView.as_view()), name='reserva_list'),
    path('crear/', login_required(ReservaCreateView.as_view()), name='reserva_create'),
    path('<int:pk>/editar/', login_required(ReservaUpdateView.as_view()), name='reserva_update'),
    path('<int:pk>/eliminar/', login_required(ReservaDeleteView.as_view()), name='reserva_delete'),
    path('<int:pk>/', login_required(ReservaDetailView.as_view()), name='reserva_detail'),
]
