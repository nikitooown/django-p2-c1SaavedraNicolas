# dispositivos/urls.py
from django.urls import path
from . import views


app_name = "dispositivos"


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("<int:dispositivo_id>/", views.detalle_dispositivo, name="detalle_dispositivo"),
    path("dispositivos/", views.catalogo, name="catalogo"),

]