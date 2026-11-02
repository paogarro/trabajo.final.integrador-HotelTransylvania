from django.shortcuts import render

# Create your views here.

from .models import Habitacion
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HabitacionListView(LoginRequiredMixin, ListView):
    model = Habitacion
    template_name = 'habitacion/list.html'
    context_object_name = 'habitacion'

class HabitacionCreateView(LoginRequiredMixin, CreateView):
    model = Habitacion
    fields = '__all__'
    template_name = 'habitacion/create.html'
    success_url = reverse_lazy('habitacion:habitacion_list')

class HabitacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Habitacion
    fields = '__all__'
    template_name = 'habitacion/update.html'
    success_url = reverse_lazy('habitacion:habitacion_list')

class HabitacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Habitacion
    template_name = 'habitacion/delete.html'
    success_url = reverse_lazy('habitacion:habitacion_list')

class HabitacionDetailView(LoginRequiredMixin, DetailView):
    model = Habitacion
    template_name = 'habitacion/detail.html'
    context_object_name = 'habitacion'
    
