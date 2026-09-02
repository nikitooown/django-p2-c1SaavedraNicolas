from django.shortcuts import render
from . import services


def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(request, "dispositivos/inicio.html", contexto)


def lista_zonas(request):
    zonas = services.resumen_zonas()
    return render(request, "dispositivos/lista_zonas.html", {"zonas": zonas})


def detalles_zona(request, zona_id):
    detalle = services.detalles_zona(zona_id)
    if detalle is None:
        return render(request, "dispositivos/zona_404.html", {"zona_id": zona_id}, status=404)
    return render(request, "dispositivos/detalles_zona.html", {"zona": detalle})