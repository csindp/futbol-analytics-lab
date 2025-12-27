# futbol-analytics-lab

Laboratorio personal para construir pipelines de datos y dashboards aplicados a fútbol:
Python → CSV/Parquet → Power BI (modelado + DAX + visualización)

## Objetivos
- Estandarizar un flujo reproducible de limpieza y exportación de datos.
- Construir métricas y modelos (star schema) para análisis de rendimiento.
- Documentar aprendizajes y decisiones técnicas.

## Estructura (propuesta)
- `src/` código principal (ETL, helpers, exports)
- `notebooks/` exploración y pruebas
- `data/` datos (no subir sensibles; usar samples)
- `reports/` salidas y resúmenes
- `docs/` documentación técnica (modelo, diccionario de datos)

## Reglas de seguridad
- No subir datos sensibles, nombres completos de menores, ni credenciales.
- Variables secretas van en `.env` (y `.env` debe estar en `.gitignore`).

## Próximos pasos
- Crear estructura base de carpetas
- Conectar repo con VS Code
- Primer script de ejemplo (export limpio)
