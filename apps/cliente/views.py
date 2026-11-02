from django.shortcuts import render

# Create your views here.

from .models import Cliente
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'cliente/list.html'
    context_object_name = 'cliente'

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/create.html'
    success_url = reverse_lazy('cliente:cliente_list')

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/update.html'
    success_url = reverse_lazy('cliente:cliente_list')

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/delete.html'
    success_url = reverse_lazy('cliente:cliente_list')

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'cliente/detail.html'
    context_object_name = 'cliente'
    
