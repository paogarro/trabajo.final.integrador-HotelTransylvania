from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.inicio.views import InicioView

app_name = 'inicio'

urlpatterns = [
    path("", login_required(InicioView.as_view()), name="inicio"),
]