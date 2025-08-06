# Fase 2 – Extracción de Datos WRF (T2 y RH2)

## Objetivo
Extraer, desde archivos WRFOUT, las variables **Temperatura a 2 m (T2)** y **Humedad Relativa a 2 m (RH2)** para todos los puntos de grilla en superficie (determinados en la Fase 1) y generar archivos de salida organizados por año y día de pronóstico.

---

## Procedimiento

### 1. Script principal
- **Archivo:** `scripts/extract_dataWRF_allxyt_year-v2.py`
- **Ejecución:** Exclusivamente en el servidor institucional `kosmos`, debido al tamaño de los archivos WRFOUT.
- **Entradas:**
  - Carpeta con archivos `wrfout` del dominio correspondiente (`WRF/D03` o `WRF/D04`).
  - Archivo `.pkl` con puntos de grilla filtrados (Fase 1).
- **Salidas:**
  - Un `.pkl` por día de pronóstico (`dia1`, `dia2`, `dia3`) para cada año procesado.
  - Formato: `WRF_DataT2RH2-allxy-allTime_diaX_{anio}.pkl`
  - Frecuencia: horaria.

---

### 2. Pre-análisis (opcional)
- **Archivo:** `notebooks/preanalisis_WRF_datos.ipynb`
- **Objetivo:** Revisar y validar rápidamente los PKL generados.
- **Funciones:**
  - Inspección de estructura y rangos de datos.
  - Serie temporal de T2 para un punto específico.
  - Mapas Folium con escala continua para T2 y RH2 en una hora seleccionada.

---

## Registro de extracción
- El progreso de años procesados se controla en el archivo:
  - `02_extraccion_datos_wrf/outputs/registro_extraccion_wrf.md`
- Este archivo contiene tablas separadas para D03 y D04, indicando:
  - Estado (`Pendiente` o `Completado`).
  - Fecha de extracción.
  - Comentarios.
- Se debe actualizar manualmente conforme avance la extracción.

---

## Archivos en esta carpeta

| Carpeta/Archivo | Descripción |
|-----------------|-------------|
| `scripts/extract_dataWRF_allxyt_year-v2.py` | Script principal de extracción (ejecutar en kosmos). |
| `outputs/registro_extraccion_wrf.md` | Registro editable de años completados/pedientes. |
| `notebooks/preanalisis_WRF_datos.ipynb` | Notebook con revisiones y visualizaciones básicas (opcional). |

---

**Nota:** Los `.pkl` resultantes **no se incluyen** en este repositorio por su tamaño; se mantienen en el servidor institucional y en equipos locales para análisis posteriores.
