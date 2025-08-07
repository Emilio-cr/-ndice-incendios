# Proyecto de Análisis y Desarrollo de Índices de Incendios

ESTRUCTURA DEL REPOSITORIO:

incendios_indices_proyecto/
│
├── 01_grillas_extraccion/       # Scripts y configuraciones para grillas (d03)
│   ├── scripts/
│   ├── docs/
│   └── outputs/
│
├── 02_extraccion_datos_wrf/
│   ├── scripts/
│   ├── docs/
│   └── outputs/
│
├── 03_datos_incendios_conaf/
│   ├── scripts/
│   ├── docs/
│   └── outputs/
│
├── 04_datos_estaciones_era5_modis/
│   ├── scripts/
│   ├── docs/
│   └── outputs/
│
├── 05_cruce_datos_modelo_validacion/
│   ├── scripts/
│   ├── docs/
│   └── outputs/
│
├── 06_cruce_datos_incendios_meteo/
│   ├── scripts/
│   ├── docs/
│   └── outputs/
│
├── 07_analisis_indices/
│   ├── scripts/
│   ├── docs/
│   └── outputs/
│
├── docs/                       # Documentación general del proyecto
│   ├── metodologia.md
│   ├── roadmap.md
│   ├── referencias.md
│
└── README.md

Este repositorio reúne scripts, documentación y resultados parciales del proyecto orientado al análisis de incendios forestales y el desarrollo de índices de riesgo, a partir de la integración de distintas fuentes de datos meteorológicos y registros históricos.

El trabajo se organiza en fases principales:

1. **Ajuste y diseño de grillas de extracción de datos (d03)**
2. **Extracción de datos del modelo WRF**
3. **Procesamiento de datos de incendios CONAF**
4. **Incorporación de datos de estaciones y otros modelos (ERA5, MODIS)**
5. **Cruce de datos y validación de salidas del modelo**
6. **Integración de datos meteorológicos y de eventos de incendios**
7. **Análisis y propuesta de implementación de índices de riesgo**

> **Nota:** Los datos originales y archivos de gran tamaño se almacenan en servidores institucionales. Este repositorio contiene únicamente scripts, documentación y salidas procesadas livianas (PKL, CSV, entre otros) que permiten la reproducción parcial de análisis.
---
