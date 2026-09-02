from django.urls import path
from . import views

app_name = "dispositivos"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("zonas/", views.lista_zonas, name="lista_zonas"),
    path("zonas/<int:zona_id>/", views.detalles_zona, name="detalles_zona"),
]