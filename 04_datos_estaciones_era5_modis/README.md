# 04_extraccion_datos_(OTRAS FUENTES)

El objetivo es generar una base de datos meteorológica paralela al modelo WRF, que permita análisis comparativos y validaciones.

## ## Fuentes de datos consideradas

- **ERA5-Land (Copernicus Climate Data Store)**: Reanálisis atmosférico con resolución espacial de 0.1°, descargado mediante la API `cdsapi`.
- **Estaciones meteorológicas disponibles**: Datos puntuales obtenidos mediante la librería `meteostat` de Python (pendiente de integrar).
- **Otros modelos satelitales y de observación** como **MODIS** (pendiente de integrar).


## Contenido (para ERA)


- `scripts/`
  - `extract-era5.py`: script principal para extraer variables meteorológicas diarias usando la API de CDS (ERA5-Land).
  - ERA5.ipynb`: notebook para definir el bounding box de extracción ajustado a la grilla WRF y visualizar los puntos de ERA5.

- `outputs/`
  - Archivos de extracción en formato NetCDF (`.nc`) por año y mes. **No se incluyen en el repositorio debido a su tamaño.**
  - `bbox_era_wrfD03.html`: Mapa interactivo que muestra el bounding box de ERA5-Land y su superposición con la grilla del dominio WRF D03.
  - `bbox_era.txt`: Archivo auxiliar con los límites geográficos del bounding box calculado, ajustado a la malla de 0.1° (N, W, S, E).

Bounding Box ajustado a ERA5-Land (resolución 0.1°):
[Norte, Oeste, Sur, Este] = [-32.4, -71.8, -33.6, -71.1]

## Variables extraídas (ERA5-Land)

- Temperatura a 2 m (`2m_temperature`)
- Temperatura de rocío a 2 m (`2m_dewpoint_temperature`)
- Componentes del viento a 10 m (`10m_u_component_of_wind`, `10m_v_component_of_wind`)
- Presión en superficie (`surface_pressure`)
- Precipitación total (`total_precipitation`)

## Notas

- La descarga se realiza por mes y año, generando un archivo `.nc` por período.
- La grilla de puntos se ajusta a una resolución de 0.1° (compatible con ERA5-Land).
- Los archivos deben ser descargados en servidores con conexión a la API de Copernicus.

