# Roadmap - Fase 01: Grillas de extracción WRF

Esta fase corresponde al diseño, extracción y validación de las grillas geográficas asociadas a los dominios D03 y D04 del modelo WRF, usadas posteriormente para extraer variables meteorológicas relevantes.

---

## Objetivos

- Extraer coordenadas de grilla (lat/lon) desde archivos `wrfout` de referencia.
- Construir DataFrames y GeoDataFrames con estructura estandarizada.
- Filtrar puntos que se encuentren dentro del área terrestre de la Región de Valparaíso.
- Generar visualizaciones interactivas para validación (mapas con Folium).
- Calcular área cubierta por los puntos de grilla sobre superficie.
- Dejar estructura de archivos y scripts reutilizable para futuros dominios o regiones.



##  Tareas completadas

- [x] Extracción de grilla D03 desde archivo `wrfout_d03_2015-05-28`
- [x] Extracción de grilla D04 desde archivo `wrfout_d04_2015-05-28`
- [x] Generación de archivos `.pkl` en formato `pandas` y `geopandas`
- [x] Filtrado de puntos dentro de la Región de Valparaíso (superficie terrestre)
- [x] Cálculo de área cubierta por cada dominio
- [x] Visualización con contornos (D03 y D04) y puntos sobre superficie
- [x] Organización de outputs y scripts

---

##  Tareas pendientes / mejoras


- [ ] Documentación detallada sobre CRS, proyecciones y transformaciones
