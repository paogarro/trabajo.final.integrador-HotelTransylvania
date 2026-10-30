from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import HotelListView, HotelCreateView, HotelUpdateView, HotelDeleteView

app_name = 'hotel'

urlpatterns = [
    path('', login_required(HotelListView.as_view()), name='hotel_list'),
    path('crear/', login_required(HotelCreateView.as_view()), name='hotel_create'),
    path('<int:pk>/editar/', login_required(HotelUpdateView.as_view()), name='hotel_update'),
    path('<int:pk>/eliminar/', login_required(HotelDeleteView.as_view()), name='hotel_delete'),
]
