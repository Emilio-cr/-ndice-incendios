# Fase 1 – Generación y Filtrado de Grillas WRF (D03 y D04)

## Objetivo
Determinar los puntos de grilla del modelo WRF en los dominios D03 y D04, filtrando aquellos ubicados sobre la superficie terrestre de la Región de Valparaíso, para su posterior uso en extracción de datos meteorológicos y análisis.

---

## Procedimiento

### 1. Extracción de grilla completa
- Archivos de entrada: `wrfout_d03` y `wrfout_d04` (no incluidos en el repositorio).
- Variables obtenidas: `i`, `j`, `lat`, `lon`.
- Salidas:
  - Formato **GeoDataFrame** (`_geo.pkl`): incluye columna `geometry` y sistema de referencia CRS.
  - Formato **DataFrame** (`.pkl`): sin columna `geometry`.

### 2. Filtrado por superficie terrestre
- Fuente cartográfica: `regiones.json`.
- Se seleccionan únicamente los puntos dentro del polígono de la **Región de Valparaíso**.
- Salidas:
  - Formato **GeoDataFrame** (`_geo.pkl`).
  - Formato **DataFrame** (`.pkl`).

### 3. Validación visual
- Mapa HTML (`dominios_y_superficie.html`) que incluye:
  - Contornos de los dominios completos (D03 en azul, D04 en verde).
  - Puntos filtrados sobre superficie en el mismo color que su dominio.

### 4. Pre-análisis numérico
- Tabla con:
  - Número de puntos sobre superficie.
  - Área cubierta por los puntos (km²).
  - Porcentaje de cobertura respecto al área total de la región.

---

## Archivos generados

| Archivo | Descripción |
|---------|-------------|
| `grilla_WRF-D03_geo.pkl` | Grilla completa D03 (GeoDataFrame) |
| `grilla_WRF-D03.pkl` | Grilla completa D03 (DataFrame) |
| `grilla_WRF-D04_geo.pkl` | Grilla completa D04 (GeoDataFrame) |
| `grilla_WRF-D04.pkl` | Grilla completa D04 (DataFrame) |
| `grilla_WRF-Superficie-D03_geo.pkl` | Grilla D03 filtrada por superficie (GeoDataFrame) |
| `grilla_WRF-Superficie-D03.pkl` | Grilla D03 filtrada por superficie (DataFrame) |
| `grilla_WRF-Superficie-D04_geo.pkl` | Grilla D04 filtrada por superficie (GeoDataFrame) |
| `grilla_WRF-Superficie-D04.pkl` | Grilla D04 filtrada por superficie (DataFrame) |
| `dominios_y_superficie.html` | Mapa comparativo de contornos y puntos filtrados |

---

**Nota:** Los archivos WRF de origen (`wrfout_...`) no se incluyen en el repositorio por su tamaño y restricciones de almacenamiento.
