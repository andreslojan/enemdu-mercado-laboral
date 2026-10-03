# Mercado laboral ecuatoriano con ENEMDU (I Trimestre 2026)

> Análisis de microdatos de la ENEMDU del INEC: indicadores laborales ponderados y validados contra las cifras oficiales, brechas por sexo y zona, informalidad e ingresos.

**Estado:** en progreso. Completado: carga, limpieza, validación y primeras cifras. Pendiente: gráficos, modelo de ingresos, dashboard e informe.

## Resumen ejecutivo (preliminar)

- Los indicadores calculados reproducen las cifras oficiales del INEC: 3 de 4 nacionales exactos, y 20 de 20 por dominio (Quito, Guayaquil, Cuenca, Machala, Ambato).
- Solo 35,7% de la PEA tiene empleo adecuado; alrededor de 32,6% está en "otro empleo no pleno" (calculado de la distribución ponderada de `condact`).
- El desempleo (3,4%) oculta la precariedad: en la zona rural es 1,7%, pero solo 18,0% de su PEA tiene empleo adecuado.
- 53,5% de los ocupados está en el sector informal (75,7% en zona rural, 41,7% en urbana).
- La mediana de ingreso laboral de las mujeres es 81,4% la de los hombres (brecha bruta, sin controles).

## Preguntas

1. ¿Cómo está compuesto el empleo en Ecuador y qué proporción es adecuado?
2. ¿Qué brechas hay por sexo, zona y educación en empleo, informalidad e ingresos?
3. ¿Cuánto rinde la educación en ingresos, y qué parte de la brecha por sexo persiste con controles? `[por completar]`

## Datos

- **Fuente:** INEC, Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU), I Trimestre 2026, base de personas (SPSS).
- **Tamaño:** 82.894 registros y 143 variables; se cargan 22 (ver `docs/diccionario_variables.md`).
- **Licencia de los datos:** Creative Commons Atribución 4.0 (INEC).
- Los microdatos no están en el repositorio.

## Metodología

- Todos los indicadores se ponderan con el factor de expansión `fexp`.
- Definiciones con `condact`: ocupados 1 a 6; PEA 1 a 8; PET 1 a 9; informalidad = sector informal (`secemp` = 2) sobre ocupados.
- Códigos especiales de `ingrl` (-1 y 999999) tratados como nulos.
- Años de estudio construidos a partir de nivel y año aprobado (regla en el diccionario; los puntos de partida 13 y 17 son una convención propia).

## Validación contra cifras oficiales

**Nacional (en % de la PEA):**

| Indicador | Calculado | INEC | Diferencia |
|---|---|---|---|
| Participación global | 63,7 | 63,8 | -0,1 |
| Empleo adecuado | 35,7 | 35,7 | 0,0 |
| Subempleo | 18,4 | 18,4 | 0,0 |
| Desempleo | 3,4 | 3,4 | 0,0 |

**Por dominio:** las 20 cifras (4 indicadores x 5 ciudades) coinciden con las publicadas. Detalle en `reports/validacion_dominios.csv`.

**Informalidad:** 53,5% de los ocupados, igual al boletín técnico del INEC.

## Resultados preliminares

| Grupo | Empleo adecuado | Subempleo | Desempleo | PEA (miles) |
|---|---|---|---|---|
| Hombres | 39,5 | 20,0 | 2,6 | 5.109 |
| Mujeres | 30,2 | 16,1 | 4,6 | 3.511 |
| Urbana | 44,9 | 18,9 | 4,2 | 5.666 |
| Rural | 18,0 | 17,4 | 1,7 | 2.954 |

| Grupo | Informalidad (% de ocupados) |
|---|---|
| Hombres | 54,6 |
| Mujeres | 52,0 |
| Urbana | 41,7 |
| Rural | 75,7 |

| | Hombres | Mujeres |
|---|---|---|
| Mediana de `ingrl` (USD) | 430 | 350 |
| Media de `ingrl` (USD) | 516,8 | 467,8 |

"El promedio nacional por sexo oculta que la brecha de informalidad tiene signo opuesto en zona urbana (hombres más informales) y rural (mujeres más informales)."

Gráficos, mapas y modelo de ingresos: `[por completar]`.

## Limitaciones

1. La participación global difiere en 0,1 puntos de la cifra publicada (63,7 frente a 63,8). Con dos definiciones de PET se obtiene el mismo valor (63,745); la causa no está identificada.
2. `ingrl` no pudo contrastarse con una cifra oficial. Se asume mensual y en dólares. Como verificación de plausibilidad, la mediana (USD 430) es cercana al SBU 2026 (USD 482) y el ingreso se comporta de forma coherente con la condición de actividad (con excepciones minoritarias que no se pudieron explicar).
3. La base trimestral es representativa por dominio, no por provincia: las sumas de `fexp` por provincia no reproducen la población esperada. No se presentan resultados provinciales con esta base.
4. Los años de estudio son una aproximación: convención propia y mezcla de sistemas educativos.
5. La brecha de ingresos presentada es bruta; no controla por horas, ocupación ni educación. `[el modelo de Mincer la ajustará]`
6. El análisis de ingresos cubre 35.302 de 39.920 ocupados (88,4%). Quedan fuera los trabajadores no remunerados y los no clasificados (3.149), que no tienen ingreso, además de 1.469 ocupados con ingreso vacío, cero o código especial. Esto introduce un sesgo de selección.
7. El diseño muestral complejo (estratos y UPM) no se modela por completo en la inferencia.
8. El análisis de ingresos cubre 35.302 de 39.920 ocupados (88,4%): se excluyen los ingresos vacíos, ceros y códigos especiales. Los trabajadores no remunerados probablemente quedan fuera (hipótesis por verificar), lo que implica un sesgo de selección.
9. Las horas de trabajo tienen valores extremos (hasta 120 por semana) que se tratarán en el modelo.

## Cómo reproducir

```
git clone https://github.com/TU_USUARIO/enemdu-mercado-laboral.git
cd enemdu-mercado-laboral
conda env create -f environment.yml
conda activate enemdu
Paquete	Versión
Python	3.11.16
pandas	3.0.6
numpy	2.4.6
statsmodels	0.15.0
geopandas	1.2.0
scikit-learn	1.9.1
```

1. Descarga la base SPSS, el diccionario, la guía de usuario y el boletín desde la página de ENEMDU Trimestral del INEC: https://www.ecuadorencifras.gob.ec/enemdu-trimestral/
2. Descomprime la base en `data/raw/spss/`.
3. Ejecuta los notebooks en orden: `01_auditoria_datos`, `02_indicadores`, `03_analisis_grupos`.

## Estructura

```
data/        (raw, interim, processed; no se versionan los microdatos)
docs/        diccionario de variables, guía, boletín, tabulados
notebooks/   exploración y validación
reports/     tablas y figuras
src/         data.py (carga, indicadores) y features.py (variables derivadas)
```

## Fuente y autor

Fuente: Instituto Nacional de Estadística y Censos (INEC), ENEMDU. Autor: `[tu nombre]` · `[LinkedIn]` · `[correo]`