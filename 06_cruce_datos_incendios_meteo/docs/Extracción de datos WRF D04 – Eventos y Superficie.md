# 🔥 Extracción de datos WRF D04 – Eventos y Superficie

En esta sección se documenta el flujo aplicado a los archivos **WRF D04** y la integración con la base de **eventos filtrados**.

---

## 📂 Archivos de entrada

- `datos-eventos-D04-filtrado-timeWRF-1ha-.pkl`  
  Eventos originales filtrados por superficie mínima (≥ 1 ha), con fecha y coordenadas.

- `WRF_DataT2RH2-SUPxy-allTime_dia1_YYYY.pkl`  
  Datos meteorológicos diarios del modelo WRF (T2, RH2, etc.) para cada año.

- `grilla_WRF-Superficie-D04_geo_idx.pkl`  
  Grilla de superficie del dominio D04 con índices `idx_coord`, `i`, `j`, `lat`, `lon`.

---

## ⚙️ Flujo de procesamiento

### 1. Asignación de coordenadas de superficie
- A partir del archivo de eventos, se busca el **punto de grilla más cercano** (`idx_coord`).
- Se construye un nuevo PKL con los eventos **georreferenciados a la grilla de superficie**.

### 2. Extracción de datos meteorológicos
- Para cada evento se selecciona una ventana de **11 días** (5 antes + día del evento + 5 después).
- Se filtran solo las coordenadas de superficie asignadas.
- Se generan archivos anuales:

eventos_wrf11dias_SUPidx_YYYY.pkl


Cada archivo contiene:
- Variables meteorológicas del WRF.
- Índice de evento (`idx_evento`).
- Índice de coordenada de superficie (`idx_coord`).
- Fechas y horas del modelo.

### 3. Combinación de resultados
- Se concatenan todos los PKL anuales en un único archivo:

eventos_wrf11dias_SUPidx_ALL.pkl


- Se genera un resumen en CSV:


con información de:
- Número de filas por evento.
- Número de días disponibles.
- Año de ocurrencia.

---

## 📄 Archivos de salida principales

| Archivo | Descripción |
|---------|-------------|
| `eventos_wrf11dias_SUPidx_YYYY.pkl` | Datos meteorológicos WRF para 11 días de cada evento (anual) |
| `eventos_wrf11dias_SUPidx_ALL.pkl`  | Concatenación de todos los años |
| `resumen_eventos_wrf11dias_SUPidx_ALL.csv` | Resumen de filas y días únicos por evento |
| `log_eventos_wrf11dias_SUPidx_ALL.txt` | Registro de ejecución y conteos básicos |

---

## 📌 Comentarios

subir los pkl de salida a driver
