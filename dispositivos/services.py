import json 
from django.conf import settings
from pathlib import Path

DATA_DIR = Path(settings.BASE_DIR) / "data"

def cargar_json(nombre_archivo):
    ruta = DATA_DIR / nombre_archivo 
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError(f"El archivo {nombre_archivo} está vacío o no contiene datos válidos.")    
    return datos

def cargar_zonas():
    return cargar_json("zonas.json")

def cargar_dispositivos():
    return cargar_json("dispositivos.json")

def cargar_categorias():
    return cargar_json("categorias.json")

def resumen_zonas():
    zonas = cargar_zonas()
    dispositivos = cargar_dispositivos()
    resumen = []
    for zona in zonas: 
        cantidad = sum(1 for d in dispositivos if d.get("zona_id") == zona["id"])
        resumen.append({
            id": zona["id"],
            "nombre": zona["nombre"],
            "cantidad_dispositivos": cantidad,
            "limite_kwh": zona["limite_kwh"],
        })
    return resumen


def detalles_zona(zona_id):
    zonas = {z["id"]: z for z in cargar_zonas()}
    zona = zonas.get(zona_id)
    if zona is None:
        return None
    
    categorias = {c["id"]: c for c in cargar_categorias()}
    dispositivos = [d for d in cargar_dispositivos() if d.get("zona_id") == zona_id]
    
    dispositivos_detalle = []
    consumo_total = 0.0
    for d in dispositivos:
        categoria = categorias.get(d.get("categoria_id"))
        consumo_total += d.get("consumo_kwh", 0)
        dispositivos_detalle.append(
            "id": d["id"],
            "nombre": d["nombre"],
            "categoria": categoria,
            "consumo_kwh": d.get("consumo_kwh", 0)
        )
    consumo_total = round(consumo_total,2)
    estado = "Alerta" if consumo_total > zona["limite_kwh"] else "Normal"
    return {
        "id": zona["id"],
        "nombre": zona["nombre"],
        "limite_kwh": zona["limite_kwh"],
        "consumo_total_kwh": consumo_total,
        "dispositivos": dispositivos_detalle,
        "estado": estado
    }


