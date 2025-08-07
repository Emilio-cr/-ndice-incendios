#  Roadmap - Fase 02: Extracción de datos WRF

Esta etapa tiene como objetivo extraer series temporales de variables meteorológicas (T2, RH2, etc.) desde archivos WRF (`wrfout`) utilizando una grilla previamente filtrada sobre la superficie.

---

## Objetivos principales

- [x] Adaptar script de extracción para lectura eficiente de archivos WRF.
- [x] Leer coordenadas de grilla filtrada (fase 01) desde archivo `.pkl`.
- [x] Procesar archivos `wrfout` por año, día y hora.
- [x] Separar series según días de pronóstico (Día 1, Día 2, Día 3).
- [x] Guardar resultados en formato `.pkl` por día de pronóstico.
- [x] Estimar tiempo de ejecución y validar funcionamiento por año.

---

##  Archivos relevantes

- `scripts/extract_dataWRF_allxyt_year-v2.py`  
  Script principal de extracción. Ejecutar en servidor institucional con acceso a archivos `wrfout`.

- `outputs/WRF_DataT2RH2-allxy-allTime_dia{1,2,3}_AÑO.pkl`  
  Archivos de salida para cada día de pronóstico y año.



---

##  Tareas completadas

| Año  | Día 1 ✅ | Día 2 ✅ | Día 3 ✅ |
|------|---------|---------|---------|
| 2015 |    ✅   |    ✅   |   ✅    |
| 2016 |    ✅   |    ✅   |   ✅    |
| 2017 |    ✅   |    ✅   |   ✅    |
| 2018 |    ✅   |    ✅   |   ✅    |

---

## ⏳ Tareas pendientes

| Año  | Día 1 🔲 | Día 2 🔲 | Día 3 🔲 |
|------|---------|---------|---------|
| 2014 |    🔲   |    🔲   |   🔲    |
| 2019 |    🔲   |    🔲   |   🔲    |
| 2020 |    🔲   |    🔲   |   🔲    |
| 2021 |    🔲   |    🔲   |   🔲    |
| 2022 |    🔲   |    🔲   |   🔲    |
| 2023 |    🔲   |    🔲   |   🔲    |
| 2024 |    🔲   |    🔲   |   🔲    |
| 2025 |    🔲   |    🔲   |   🔲    |


---

## 🧪 Verificación y análisis

- [x] Script complementario de análisis rápido de salidas (`analisis_salida_WRF.ipynb`)
  - Verifica estructura del DataFrame.
  - Grafica series de temperatura.
  - Visualiza mapas por hora fija.
- [ ] Revisión visual por año (uno por uno).

---

##  Notas

- No se suben archivos `.pkl` de salida al repositorio por su tamaño. Se almacenan en:
  -  Servidor institucional (`/WRF/D03/`, `/WRF/D04/`)
  - Almacenamiento local del usuario

- El script requiere `netCDF4`, `wrf-python`, `pandas` y acceso al archivo de grilla (`grilla_WRF_superficie_idx.pkl`).

---

##  Próximos pasos

- [ ] Completar extracción para todos los años.
- [ ] Automatizar validación por año con scripts ligeros.
- [ ] Incluir resumen de cobertura temporal y espacial.
