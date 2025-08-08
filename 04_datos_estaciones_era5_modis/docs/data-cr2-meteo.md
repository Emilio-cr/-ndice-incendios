# Datos Meteorológicos desde CR2

Este documento recopila información sobre fuentes de datos meteorológicos alternativas. Se centra en productos generados por el Centro de Ciencia del Clima y la Resiliencia (CR2), disponibles públicamente desde su plataforma oficial.

El objetivo es dejar registro de los productos descargados, sus características técnicas principales, el uso potencial en el proyecto, y las referencias asociadas.

---

## 1. Descripción General

CR2 pone a disposición múltiples bases de datos meteorológicas y climatológicas para Chile, que incluyen observaciones, interpolaciones y productos derivados.


---

## 2. Productos descargados

### 2.1. CR2MET PRODUCTOS GRILLADOS– Precipitación y Temperaturas extremas (v2.5)

**Enlace oficial**: https://www.cr2.cl/datos-productos-grillados/

**Descripción**:  
CR2MET incluye productos diarios distribuidos espacialmente de precipitación y temperatura máxima/mínima sobre el territorio continental chileno. Está disponible en una grilla regular de **0.05° lat/lon**, abarcando el período **1960–2021**.

- Datos derivados mediante modelos estadísticos calibrados con observaciones.
- Insumos: reanálisis ERA5, topografía, y temperatura superficial MODIS.
- Variables:  
  - `pr_day`: precipitación diaria  
  - `tasmax_day`: temperatura máxima diaria  
  - `tasmin_day`: temperatura mínima diaria

**Archivos descargados**:
- `CR2MET_v2.5_pr_day_1960_2021.nc` (precipitación diaria)

**Referencias para citar**:  
> Juan P. Boisier. (2023). *CR2MET: A high-resolution precipitation and temperature dataset for the period 1960–2021 in continental Chile* (v2.5) [Data set]. Zenodo.  
> DOI: [10.5281/zenodo.7529682](https://doi.org/10.5281/zenodo.7529682)  
> DOI general (última versión): [10.5281/zenodo.7529681](https://doi.org/10.5281/zenodo.7529681)

---

### 2.2. CR2  DATA CLIMA -Precipitación Diaria – Estaciones 

**Enlace oficial**: https://www.cr2.cl/datos-de-precipitacion/

**Descripción**:  
Conjunto de datos de **precipitación acumulada diaria y mensual** obtenidos de estaciones meteorológicas desde 1930 a 2020.

- Precipitación diaria: 816 estaciones (783 DGA + 33 DMC)
- Precipitación mensual: 1145 estaciones (incluye datos de anuarios)

**Estándar horario**:  
Los datos diarios se reportan en el intervalo **(12:00–12:00] UTC**, equivalente a **08:00 AM – 08:00 AM hora local (GMT-4)**.  
El total diario se construye a partir de cuatro bloques horarios UTC: 12–18, 18–00, 00–06 y 06–12.

**Archivos descargados**:
- `ccr2_prDaily_2018.zip`  
PERIODO: Enero de 1900 - Marzo de 2018.
Resolución Temporal: Diaria
REGION: 874 estaciones de todo Chile
VARIABLES: precipitación acumulada diaria, medida en milímetros.


**Referencias para citar**:  

---

## 3. Registro de documentación y archivos descargados

| Producto         | Variable        | Archivo descargado                         | Año(s)       | Tamaño aprox. | Notas                     |
|------------------|------------------|---------------------------------------------|---------------|----------------|----------------------------|
| CR2MET v2.5      | Precipitación    | CR2MET_v2.5_pr_day_1960_2021.nc             | 1960–2021     |                |                            |
| CR2 Estaciones   | Precipitación    | cr2_prDaily_2018.zip                        | 1900 - 2018   |  16 Mb         |                            |
| CR2MET v2.5      | Temperaturas     | (pendiente)                                 |               |                |                            |
| [Producto futuro] | [var]            | (pendiente)                                |               |                |                            |

---

## 4. Observaciones


---
