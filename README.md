# Webos🥚
Sistema Experto de Clasificación de Calidad de Huevos utilizando Lógica Difusa (Mamdani).

Este sistema utiliza un motor de inferencia matricial para categorizar huevos en tres clases (A, B y C) basado en variables físicas, clasificadas ent la estética, la frescura y la integridad estructural.

## Ejecución

. **Ejecutar la Clasificación:**
   Corre el flujo principal para ver los resultados y estadísticas:
   ```bash
   python3 main.py
   ```

## Analizador

```python
from analizador import AnalizadorCalidad

# carga el analizador
analizador = AnalizadorCalidad(resultados)

# estadísticas generales
analizador.imprimir_estadisticas()

# Filtrar por clase
huevos_clase_a = analizador.filtrar_por_clase("Clase A")

# Ordenar por calidad (centroide) de mejor a peor
mejores_huevos = analizador.ordenar_por_centroid(ascendente=False)

# huevo específico por ID
huevo_especifico = analizador.obtener_por_id(42)

# Imprimir tabla de reporte detallada
analizador.imprimir_reporte_completo()
```

## Lógica Matricial

El sistema no evalúa las 6 variables de forma aislada, sino que las agrupa en **Bloques Lógicos**:
1.  **Bloque Cáscara:** Grosor + Rugosidad.
2.  **Bloque Frescura:** Densidad + Cámara de Aire.
3.  **Bloque Estética:** Manchas + Forma.

*Desarrollado como parte del proyecto de Introducción Inteligencia Artificial - Aplicación*
