# IA.md — Registro de uso de IA (Fase 1 EcoEnergy)

**Herramienta utilizada:** Claude (Anthropic), vía chat web.

## Qué le pedí

1. Revisión del código inicial de mi app `dispositivos` (services.py, views.py, urls.py, JSON) contra la pauta de la Fase 1, para identificar qué faltaba respecto al modelo de Zonas.
2. Guía paso a paso para reestructurar el proyecto hacia el modelo Zona–Dispositivo–Categoría (sin que la IA escribiera el código por mí directamente en un primer momento).
3. Revisión y corrección de errores de sintaxis que cometí yo mismo al escribir `services.py` (comillas faltantes, diccionarios mal formados en `dispositivos_detalle.append(...)`).
4. Ayuda para resolver un conflicto de merge en Git (`services.py`, `views.py`, `urls.py`) generado porque trabajé por error en una carpeta de repositorio duplicada.
5. Plantillas de templates HTML con Bootstrap 5 (`base.html`, `lista_zonas.html`, `detalles_zona.html`, `zona_404.html`).
6. Estructura de este mismo archivo (`IA.md`) y de `README.md`/`ANALISIS.md`.

## Qué usé tal cual

- La estructura de los templates HTML (`lista_zonas.html`, `detalles_zona.html`, `zona_404.html`, navbar en `base.html`), adaptando clases de Bootstrap 5 sugeridas.
- El texto amigable de la página 404 ("Ups, esa zona no existe").

## Qué escribí o corregí yo mismo

- `zonas.json`, `categorias.json`, `dispositivos.json`: los redacté yo con los datos de ejemplo, definiendo cuántas zonas/dispositivos y con qué límites, para poder probar los casos NORMAL, ALERTA y zona vacía.
- `services.py` y `views.py`: los escribí yo mismo siguiendo la guía; la IA señaló errores de sintaxis puntuales (llaves faltantes, nombres de función que no coincidían entre `services.py` y `views.py`) que corregí yo en mi propio código.
- Resolví manualmente los conflictos de merge en el editor, aceptando mi versión (`HEAD`) sobre la versión antigua del repositorio duplicado.
- Verifiqué cada cambio corriendo `python manage.py check` y probando las rutas `/`, `/zonas/`, `/zonas/1/`, `/zonas/5/`, `/zonas/999/` en el navegador antes de comitear.

## Cómo lo verifiqué

- `python manage.py check` sin errores en cada etapa.
- Prueba manual en navegador de las 5 rutas clave, confirmando estados NORMAL/ALERTA, zona vacía y 404 controlado.
- Prueba de CA-06: agregué un dispositivo nuevo a `dispositivos.json` y confirmé que apareció sin tocar código.

Declaro que comprendo el funcionamiento de cada archivo entregado y puedo explicarlo en la evaluación.