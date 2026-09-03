# ANALISIS.md — EcoEnergy Fase 1

## 1. Relaciones y multiplicidades

El modelo de datos sigue el diagrama UML entregado en el enunciado (Figura 1):

- **Zona 1 — 0..\* Dispositivo**: una zona puede tener cero o más dispositivos; cada dispositivo pertenece a exactamente una zona.
- **Categoría 1 — 0..\* Dispositivo**: una categoría puede clasificar cero o más dispositivos; cada dispositivo pertenece a exactamente una categoría.

Las relaciones se implementan mediante identificadores en los archivos JSON, no con Foreign Keys de Django (no se usan Models en esta fase).

## 2. Claves de conexión

| Archivo | Clave propia | Clave(s) foránea(s) |
|---|---|---|
| `zonas.json` | `id` | — |
| `categorias.json` | `id` | — |
| `dispositivos.json` | `id` | `zona_id` (referencia a `zonas.json`), `categoria_id` (referencia a `categorias.json`) |

Todo `zona_id` y `categoria_id` presente en `dispositivos.json` corresponde a un `id` existente en su archivo respectivo. `services.py` resuelve estas relaciones en memoria mediante diccionarios Python (`{id: objeto}`), sin usar ORM.

## 3. Matriz Criterio de aceptación | Archivo/Componente | Prueba

| Criterio | Archivo/Componente | Prueba realizada |
|---|---|---|
| CA-01 | `views.py` (`lista_zonas`), `services.py` (`resumen_zonas`) | Se visitó `/zonas/` y se verificó que aparecen las 5 zonas de `zonas.json`. |
| CA-02 | `templates/dispositivos/lista_zonas.html` | Cada tarjeta muestra nombre, límite, cantidad de dispositivos y botón "Ver detalle" hacia `/zonas/<id>/`. |
| CA-03 | `templates/dispositivos/detalles_zona.html`, `services.py` (`detalles_zona`) | Se visitó `/zonas/2/` (Oficinas Administrativas) y se comprobó que muestra dispositivos, categoría, consumo y estado. |
| CA-04 | `services.py` (`detalles_zona`) | El consumo total se calcula sumando `consumo_kwh` de los dispositivos en tiempo de ejecución; no hay valores escritos a mano en el HTML. |
| CA-05 | `services.py` (`detalles_zona`) | Oficinas Administrativas: consumo total 39.5 kWh > límite 30.0 kWh → se muestra ALERTA. Bodega Norte: consumo menor al límite → se muestra NORMAL. |
| CA-06 | `services.py` | Se agregó un dispositivo nuevo a `dispositivos.json` y se recargó `/zonas/<id>/`: apareció automáticamente, sin modificar código. |
| CA-07 | `services.py`, `templates/dispositivos/detalles_zona.html` | Zona "Estacionamiento" (`/zonas/5/`) no tiene dispositivos asociados; se muestra el mensaje "Esta zona no tiene dispositivos" en vez de una tabla vacía. |
| CA-08 | `views.py` (`detalles_zona`), `templates/dispositivos/zona_404.html` | Se visitó `/zonas/999/` (id inexistente): responde con página 404 personalizada, código de estado 404, sin traza técnica. |
| CA-09 | `templates/base.html` | Al aumentar la cantidad de zonas/dispositivos, la navegación (navbar) y el contenido se mantienen accesibles. |
| CA-10 | `templates/dispositivos/detalles_zona.html` | La tabla de dispositivos usa `.table-responsive`, permitiendo desplazamiento horizontal sin desbordar la página. |
| CA-11 | `templates/base.html` y todos los templates | Header (navbar verde), títulos, tarjetas, tablas y botones mantienen un estilo Bootstrap coherente en todas las páginas. |
| CA-12 | `templates/dispositivos/detalles_zona.html` | El estado usa texto ("NORMAL"/"ALERTA") + color del badge, no solo color. |
| CA-13 | Proyecto completo | `python manage.py check` se ejecutó sin errores |