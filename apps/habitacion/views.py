from django.shortcuts import render

# Create your views here.

from .models import Habitacion
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class HabitacionListView(ListView):
    model = Habitacion
    template_name = 'habitacion/list.html'
    context_object_name = 'habitacion'

class HabitacionCreateView(CreateView):
    model = Habitacion
    fields = '__all__'
    template_name = 'habitacion/create.html'
    success_url = reverse_lazy('habitacion:habitacion_list')

class HabitacionUpdateView(UpdateView):
    model = Habitacion
    fields = '__all__'
    template_name = 'habitacion/update.html'
    success_url = reverse_lazy('habitacion:habitacion_list')

class HabitacionDeleteView(DeleteView):
    model = Habitacion
    template_name = 'habitacion/delete.html'
    success_url = reverse_lazy('habitacion:habitacion_list')
    
