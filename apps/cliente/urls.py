from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, ClienteDetailView

app_name = 'cliente'

urlpatterns = [
    path('', login_required(ClienteListView.as_view()), name='cliente_list'),
    path('crear/', login_required(ClienteCreateView.as_view()), name='cliente_create'),
    path('<int:pk>/editar/', login_required(ClienteUpdateView.as_view()), name='cliente_update'),
    path('<int:pk>/eliminar/', login_required(ClienteDeleteView.as_view()), name='cliente_delete'),
    path('<int:pk>/', login_required(ClienteDetailView.as_view()), name='cliente_detail'),
]
