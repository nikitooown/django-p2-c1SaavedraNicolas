import json
from django.conf import settings
from django.shortcuts import render

def cargar_dispositivos():
    ruta = settings.BASE_DIR / "data" / "dispositivos.json"

    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)

    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de dispositivos")
    return datos


def catalogo(request):
    dispositivos = cargar_dispositivos()

    activos = sum(
        1 for item in dispositivos
         if item["estado"] == "Activo"
    )
    contexto = {
        "dispositivos": dispositivos,
        "total": len(dispositivos),
        "total_activos": activos,
    }
    return render(
        request, "dispositivos/catalogo.html", contexto
    )
