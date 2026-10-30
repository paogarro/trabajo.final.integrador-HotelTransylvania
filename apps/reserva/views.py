from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Reserva


class ReservaListView(ListView):
    model = Reserva
    template_name = 'reserva/list.html'
    context_object_name = 'reserva'


class ReservaCreateView(CreateView):
    model = Reserva
    fields = '__all__'
    template_name = 'reserva/create.html'
    success_url = reverse_lazy('reserva:reserva_list')


class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = '__all__'
    template_name = 'reserva/update.html'
    success_url = reverse_lazy('reserva:reserva_list')


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'reserva/delete.html'
    success_url = reverse_lazy('reserva:reserva_list')
