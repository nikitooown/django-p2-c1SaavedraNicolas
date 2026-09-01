from django.shortcuts import render
from django.http import HttpResponse
from . import services

def inicio(request):
    contexto = {
        
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }

    return render(request, "dispositivos/inicio.html", contexto)

def lista_zonas(request):
    zonas = services.obtener_resumen_zonas()

    return render(request, "dispositivos/lista_zonas.html", {"zonas": zonas})

def detalles_zona(request, zona_id):
    detalle = services.obtener_detalles_zona(zona_id)
    if detalle is None:
        return HttpResponse("Zona no encontrada", status=404)       
    return render(request, "dispositivos/detalles_zona.html", {"detalle": detalle})


