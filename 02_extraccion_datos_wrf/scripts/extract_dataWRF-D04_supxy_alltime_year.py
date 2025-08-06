"""
===========================================================
Extracción de T2 y RH2 desde archivos WRFOUT (dominio D04)
===========================================================

Descripción:
------------
Este script lee todos los archivos WRFOUT disponibles para un año
específico en el dominio D04 y extrae las variables:

- T2  → Temperatura a 2 m (°C)
- RH2 → Humedad relativa a 2 m (%)
- HGT → Altura del punto de grilla (m)

Se procesan únicamente los puntos de grilla en superficie
determinados previamente (archivo PKL de grilla filtrada).
Los resultados se separan por día de pronóstico (Día 1, Día 2, Día 3)
y se guardan en tres PKL independientes.

Requisitos:
-----------
- Ejecutar en el servidor institucional **kosmos** (por tamaño de datos).
- Archivos WRFOUT accesibles en la carpeta `WRF/D04`.
- Archivo PKL `grilla_WRF_superficie_idx.pkl` con índices i/j, lat, lon.

Salidas:
--------
- `WRF_DataT2RH2-allxy-allTime_dia1_{anio}.pkl`
- `WRF_DataT2RH2-allxy-allTime_dia2_{anio}.pkl`
- `WRF_DataT2RH2-allxy-allTime_dia3_{anio}.pkl`
"""

import pandas as pd
from netCDF4 import Dataset
from wrf import getvar, ALL_TIMES
import glob, os, time

# ============================
# Configuración inicial
# ============================
inicio = time.time()  # Temporizador de ejecución

# Ruta base a los WRFOUT en el servidor
ruta_wrf = "WRF/D04"  # Carpeta en kosmos

# Archivo con índices de grilla filtrada (superficie)
archivo_pkl = "grilla_WRF_superficie_idx_simple.pkl"

# Año a procesar
anio = 2022

# ============================
# Cargar puntos de grilla
# ============================
puntos = pd.read_pickle(archivo_pkl)
iy_list = puntos['iy'].to_numpy()
ix_list = puntos['ix'].to_numpy()
lat_list = puntos['lat'].to_numpy()
lon_list = puntos['lon'].to_numpy()

# ============================
# Listar archivos WRFOUT
# ============================
archivos_wrf = sorted(glob.glob(os.path.join(ruta_wrf, f"wrfout_d04_{anio}-*")))
print(f"[INFO] Archivos encontrados: {len(archivos_wrf)}", flush=True)

# Almacenes para datos separados por día de pronóstico
datos_d1, datos_d2, datos_d3 = [], [], []

# ============================
# Procesar archivos WRF
# ============================
for idx_archivo, archivo in enumerate(archivos_wrf, start=1):
    try:
        tiempo_actual = time.time() - inicio
        print(f"[INFO] Procesando archivo {idx_archivo}/{len(archivos_wrf)}: {os.path.basename(archivo)}", flush=True)
        print(f"       Tiempo transcurrido: {tiempo_actual/60:.2f} min", flush=True)

        # Abrir archivo NetCDF
        ncfile = Dataset(archivo)

        # Variables a extraer
        t2 = getvar(ncfile, "T2", timeidx=ALL_TIMES) - 273.15  # Convertir a °C
        rh2 = getvar(ncfile, "rh2", timeidx=ALL_TIMES)          # %
        hgt = getvar(ncfile, "HGT", timeidx=0)                  # m

        # Construir eje temporal
        start_date = pd.to_datetime(ncfile.START_DATE.replace("_", " "))
        tiempos = pd.to_timedelta(ncfile.variables["XTIME"][:], unit="m") + start_date

        # Recorrer todos los tiempos disponibles
        for tidx, tiempo in enumerate(tiempos):
            horas = (tiempo - tiempos[0]).total_seconds() / 3600

            # Seleccionar lista de destino según el día de pronóstico
            if horas < 24:
                lista_dest = datos_d1
            elif horas < 48:
                lista_dest = datos_d2
            elif horas < 72:
                lista_dest = datos_d3
            else:
                continue

            # Guardar datos para cada punto de grilla
            for iy, ix, lat, lon in zip(iy_list, ix_list, lat_list, lon_list):
                lista_dest.append({
                    "fecha_modelo": tiempo.date(),
                    "hora": tiempo.hour,
                    "lat": lat,
                    "lon": lon,
                    "HGT": float(hgt[iy, ix]),
                    "T2":  float(t2[tidx, iy, ix]),
                    "RH2": float(rh2[tidx, iy, ix])
                })

        ncfile.close()

    except Exception as e:
        print(f"[ERROR] Procesando {archivo}: {e}", flush=True)
        continue

# ============================
# Guardar resultados
# ============================
pd.DataFrame(datos_d1).to_pickle(f"WRF_DataT2RH2-allxy-allTime_dia1_{anio}.pkl")
pd.DataFrame(datos_d2).to_pickle(f"WRF_DataT2RH2-allxy-allTime_dia2_{anio}.pkl")
pd.DataFrame(datos_d3).to_pickle(f"WRF_DataT2RH2-allxy-allTime_dia3_{anio}.pkl")

# ============================
# Resumen final
# ============================
fin = time.time()
print("\n[INFO] Guardado completo:", flush=True)
print(f"Día 1: {len(datos_d1)} registros", flush=True)
print(f"Día 2: {len(datos_d2)} registros", flush=True)
print(f"Día 3: {len(datos_d3)} registros", flush=True)
print(f"Tiempo total de ejecución: {(fin - inicio)/60:.2f} minutos", flush=True)
