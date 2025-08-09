# Procesamiento de eventos de incendios CONAF – GitHub Repo

Este repositorio contiene herramientas para procesar y filtrar datos oficiales de incendios forestales proporcionados por CONAF (procesados por el CR2), con el objetivo de preparar insumos para análisis en dominios del modelo WRF.  

La primera etapa de trabajo se realiza en el notebook **`git-Data-eventos.ipynb`**, ubicado en la carpeta `scripts/`.  
Este notebook realiza:

- Integración de la base de datos nacional de incendios (2002–2020).
- Filtrado por **Región de Valparaíso**.
- Filtrado espacial para los dominios **WRF D03 y D04** usando grillas de superficie.
- Exportación de resultados en formatos `pandas` y `GeoPandas`.
- Inspecciones visuales preliminares con mapas interactivos (`folium`).
- Resumen estadístico inicial por dominio y por umbrales de superficie quemada.

---

## 📂 Archivos de salida

Todos los archivos generados se almacenan en la carpeta `outputs/`:

| Archivo                                          | Descripción |
|--------------------------------------------------|-------------|
| `datos-CONAF-PAIS.pkl`                           | Base nacional de incendios. |
| `datos-CONAF-VREGION.pkl`                        | Eventos filtrados para la Región de Valparaíso. |
| `datos-CONAF-VREGION-D03_geo.pkl`                | Eventos en D03 con geometría (GeoDataFrame). |
| `datos-CONAF-VREGION-D03.pkl`                    | Eventos en D03 tabular (pandas). |
| `datos-CONAF-VREGION-D04_geo.pkl`                | Eventos en D04 con geometría (GeoDataFrame). |
| `datos-CONAF-VREGION-D04.pkl`                    | Eventos en D04 tabular (pandas). |
| `mapa_D03_incendios_mayor10ha.html` *(opcional)* | Mapa Folium de eventos ≥10 ha en D03. |
| `mapa_D04_incendios_mayor10ha.html` *(opcional)* | Mapa Folium de eventos ≥10 ha en D04. |

---

## 📚 Fuente de datos

- **Base de datos**: Datos oficiales de incendios forestales de CONAF procesados por el Centro de Ciencia del Clima y la Resiliencia (CR2).
- **Repositorio de origen**: [Datos para la Resiliencia – CONAF Incendios](https://datospararesiliencia.cl/dataset.xhtml?persistentId=doi%3A10.71578%2FUXAUN5&version=&q=&fileTypeGroupFacet=&fileAccess=&fileTag=%22geojson%22&fileSortField=&fileSortOrder=&tagPresort=false&folderPresort=true)
- **Cobertura temporal**: Temporadas 2002–2003 a 2019–2020.
- **Formato original**: Archivos `.csv` (delimitador `|`) organizados por carpeta y temporada.

---

## 📌 Próximos pasos

Como parte de la siguiente etapa (segundo notebook de esta sección) se desarrollará:

- Pre-análisis de tipos de eventos y sus causas.
- Resumen estadístico ampliado con gráficas.
- Análisis temporal y espacial de eventos significativos.
- Preparación de visualizaciones comparativas entre dominios WRF.

---

## 📁 Estructura del repositorio

