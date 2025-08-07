# Proyecto de Análisis de Incendios

Este repositorio reúne scripts, documentación y resultados parciales del proyecto orientado al análisis de incendios forestales y al desarrollo de índices de riesgo, a partir de la integración de distintas fuentes de datos meteorológicos y registros históricos.

## Objetivo general

Diseñar una metodología para caracterizar condiciones meteorológicas asociadas a incendios en la Región de Valparaíso, integrando información de modelos numéricos (WRF, ERA5, MODIS), estaciones meteorológicas y datos históricos de incendios forestales.

## Estructura del proyecto

El trabajo se organiza en **7 fases principales**, cada una contenida en una carpeta específica del repositorio:

1. **`01_grillas_extraccion/`**  
   Ajuste y diseño de grillas de extracción (dominios D03 y D04 del modelo WRF).
   
2. **`02_extraccion_datos_wrf/`**  
   Extracción de variables meteorológicas (T2, RH2) (otras variables) desde archivos `wrfout`, sobre puntos de grilla en superficie.

3. **`03_datos_incendios_conaf/`**  
   Procesamiento, limpieza y filtrado de registros históricos de incendios forestales (CONAF).

4. **`04_datos_estaciones_era5_modis/`**  
   Incorporación de datos externos desde estaciones meteorológicas, ERA5 y MODIS.

5. **`05_cruce_datos_modelo_validacion/`**  
   Validación de salidas del modelo WRF mediante comparación con datos observacionales.

6. **`06_cruce_datos_incendios_meteo/`**  
   Integración de información meteorológica y de eventos de incendios para análisis conjunto.

7. **`07_analisis_indices/`**  
   Análisis, diseño y evaluación de índices meteorológicos de riesgo de incendios.

---

> **Nota importante:**  
> Los archivos originales de gran tamaño (archivos WRF, bases completas de incendios, datos satelitales crudos) se almacenan en servidores institucionales y **no están incluidos en este repositorio**.  
> Aquí se incluyen solamente:
> - Scripts principales (`.py`, `.ipynb`)  
> - Documentación en texto (`.md`)  
> - Archivos de salida procesados livianos (`.pkl`, `.csv`)  
> - Mapas en formato `.html` para inspección visual

---
