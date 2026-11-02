from django.shortcuts import render

# Create your views here.

from .models import ActividadTuristica
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class ActividadListView(LoginRequiredMixin, ListView):
    model = ActividadTuristica
    template_name = 'actividad_turistica/list.html'
    context_object_name = 'actividad'

class ActividadCreateView(LoginRequiredMixin, CreateView):
    model = ActividadTuristica
    fields = '__all__'
    template_name = 'actividad_turistica/create.html'
    success_url = reverse_lazy('actividad_turistica:actividad_turistica_list')

class ActividadUpdateView(LoginRequiredMixin, UpdateView):
    model = ActividadTuristica
    fields = '__all__'
    template_name = 'actividad_turistica/update.html'
    success_url = reverse_lazy('actividad_turistica:actividad_turistica_list')

class ActividadDeleteView(LoginRequiredMixin, DeleteView):
    model = ActividadTuristica
    template_name = 'actividad_turistica/delete.html'
    success_url = reverse_lazy('actividad_turistica:actividad_turistica_list')

class ActividadDetailView(LoginRequiredMixin, DetailView):
    model = ActividadTuristica
    template_name = 'actividad_turistica/detail.html'
    context_object_name = 'actividad'
    