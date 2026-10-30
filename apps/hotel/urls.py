from django.urls import path
from .views import HotelListView, HotelCreateView, HotelUpdateView, HotelDeleteView

app_name = 'hotel'

urlpatterns = [
    path('', HotelListView.as_view(), name='hotel_list'),
    path('crear/', HotelCreateView.as_view(), name='hotel_create'),
    path('<int:pk>/editar/', HotelUpdateView.as_view(), name='hotel_update'),
    path('<int:pk>/eliminar/', HotelDeleteView.as_view(), name='hotel_delete'),
]
