from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Reserva


class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'reserva/list.html'
    context_object_name = 'reserva'


class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    fields = '__all__'
    template_name = 'reserva/create.html'
    success_url = reverse_lazy('reserva:reserva_list')


class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reserva
    fields = '__all__'
    template_name = 'reserva/update.html'
    success_url = reverse_lazy('reserva:reserva_list')


class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = 'reserva/delete.html'
    success_url = reverse_lazy('reserva:reserva_list')

class ReservaDetailView(LoginRequiredMixin, DetailView):
    model = Reserva
    template_name = 'reserva/detail.html'
    context_object_name = 'reserva'
