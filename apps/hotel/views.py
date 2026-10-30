from django.shortcuts import render

# Create your views here.

from .models import Hotel
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel/list.html'
    context_object_name = 'hotel'

class HotelCreateView(CreateView):
    model = Hotel
    fields = '__all__'
    template_name = 'hotel/create.html'
    success_url = reverse_lazy('hotel:hotel_list')

class HotelUpdateView(UpdateView):
    model = Hotel
    fields = '__all__'
    template_name = 'hotel/update.html'
    success_url = reverse_lazy('hotel:hotel_list')

class HotelDeleteView(DeleteView):
    model = Hotel
    template_name = 'hotel/delete.html'
    success_url = reverse_lazy('hotel:hotel_list')
    
