from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(
        request,
        "dispositivos/inicio.html",
        contexto,
    )


def detalle_dispositivo(request, dispositivo_id):
    # Simulamos que solo el dispositivo con ID 1 existe
    if dispositivo_id == 1:
        return HttpResponse(f"<h1>Dispositivo Encontrado</h1><p>Detalles del Dispositivo #{dispositivo_id}: Panel Solar Activo</p>", status=200)

    # Cualquier otro ID responde con 404
    return HttpResponse("<h1>Error 404</h1><p>Dispositivo no encontrado</p>", status=404)


def catalogo(request):
    dispositivos = [
        {"nombre": "Medidor inteligente", "estado": "Activo", "consumo_kwh": 45.5},
        {"nombre": "Sensor de temperatura", "estado": "Activo", "consumo_kwh": 12.0},
        {"nombre": "Climatizador", "estado": "Revisión", "consumo_kwh": 110.2},
                {"nombre": "Climatizador", "estado": "Revisión", "consumo_kwh": 110.2},
    ]

    total = len(dispositivos)
    total_activos = sum(1 for d in dispositivos if d.get("estado") == "Activo")

    contexto = {
        "dispositivos": dispositivos,
        "total": total,
        "total_activos": total_activos,
    }

    return render(
        request,
        "dispositivos/catalogo.html",
        contexto,
    )
