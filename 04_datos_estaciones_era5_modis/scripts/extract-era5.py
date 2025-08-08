import cdsapi
import os

# === 1. Inicializar cliente de descarga de Copernicus ===
c = cdsapi.Client()

# === 2. Carpeta de salida ===
out_dir = "era5land_daily_d03"  # Nombre del directorio
os.makedirs(out_dir, exist_ok=True)

# === 3. Bounding box (Norte, Oeste, Sur, Este) ===
# Ajustado a la malla de resolución 0.1° para cubrir el dominio D03
bbox_era = [-32.3, -71.9, -33.6, -71.0]

# === 4. Variables meteorológicas a descargar ===
variables = [
    "2m_dewpoint_temperature",
    "2m_temperature",
    "10m_u_component_of_wind",
    "10m_v_component_of_wind",
    "surface_pressure",
    "total_precipitation"  
]


# === 5. Iterar por año y mes ===
for year in range(2014, 2020):  # Rango de años: 2014–2019
    for month in range(1, 13):  # Meses 1–12

        # Nombre del archivo de salida
        target_file = os.path.join(out_dir, f"era5land_daily_{year}_{month:02d}.nc")

        # Saltar si ya fue descargado
        if os.path.exists(target_file):
            print(f"{target_file} ya existe, saltando...")
            continue

        # Lista genérica de días (1 al 31) — el servidor ignora días inválidos
        days = [f"{d:02d}" for d in range(1, 32)]

        print(f"Descargando {year}-{month:02d}...")

        try:
            c.retrieve(
                "derived-era5-land-daily-statistics",
                {
                    "variable": variables,
                    "year": str(year),
                    "month": f"{month:02d}",
                    "day": days,
                    "daily_statistic": "daily_mean",
                    "time_zone": "utc+00:00",
                    "frequency": "1_hourly",
                    "area": bbox_era,
                    "data_format": "netcdf",
                    "download_format": "unarchived"
                },
                target_file
            )

        except Exception as e:
            print(f"Error en {year}-{month:02d}: {e}")