from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>EcoEnergy</h1><p>Back End en funcionamiento</p>")

def detalle_dispositivo(request, dispositivo_id):
    # Simulamos que solo el dispositivo con ID 1 existe
    if dispositivo_id == 1:
        return HttpResponse(f"<h1>Dispositivo Encontrado</h1><p>Detalles del Dispositivo #{dispositivo_id}: Panel Solar Activo</p>", status=200)
    
    # Cualquier otro ID responde con 404
    return HttpResponse("<h1>Error 404</h1><p>Dispositivo no encontrado</p>", status=404)