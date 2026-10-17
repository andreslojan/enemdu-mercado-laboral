# Diccionario de variables: ENEMDU I Trimestre 2026

Fuente: INEC, ENEMDU, base de personas (SPSS `.sav`). Este diccionario cubre solo las 22 variables que usa el proyecto (`COLUMNAS` en `src/data.py`) y las derivadas en `src/features.py`.

Convención de estado: **Verificado** = comprobado con los datos o con una cifra oficial del INEC. **Documentado** = tomado de la metodología oficial (Castillo y Rosero, 2015). **Hipótesis** = interpretación mía sin verificación oficial.

## 1. Diseño muestral y ponderación

| Variable | Descripción | Estado |
|---|---|---|
| `fexp` | Factor de expansión. Todos los indicadores se ponderan con él (razón de sumas de pesos). | Verificado |
| `upm` | Unidad primaria de muestreo. Se usa para agrupar errores estándar. | Verificado |
| `estrato` | Estrato de muestreo. Cada UPM pertenece a un solo estrato. | Verificado |
| `dominio` | Dominio de estudio (5 ciudades autorrepresentadas y resto del país). Cada estrato pertenece a un solo dominio. La base es representativa por dominio, no por provincia. | Verificado |
| `conglomerado` | Identificador de conglomerado. No se usa en el análisis. | Documentado |
| `area` | Área: urbano o rural. | Verificado |
| `ciudad` | Código de ciudad/provincia. El catálogo de códigos no se pudo resolver, por eso no se usa para análisis geográfico. | Pendiente |

Anidamiento verificado en el cuaderno 01: UPM dentro de estrato, estrato dentro de dominio (máximo 1 en ambos casos).

## 2. Condición de actividad (`condact`)

Definiciones según la metodología oficial del INEC. Umbrales: 40 horas semanales (30 para 15 a 17 años) y salario básico unificado (SBU).

| Código | Categoría | Definición | Grupo |
|---|---|---|---|
| 0 | Menores de 15 años | Fuera de la población en edad de trabajar | No PET |
| 1 | Empleo adecuado | 40 horas o más e ingreso igual o superior al SBU; o menos de 40 horas, ingreso igual o superior al SBU y sin deseo de trabajar más | Ocupado |
| 2 | Subempleo por tiempo | Menos de 40 horas, desea y está disponible para trabajar más; cualquier nivel de ingreso | Ocupado |
| 3 | Subempleo por ingresos | 40 horas o más, ingreso inferior al SBU y desea trabajar más | Ocupado |
| 4 | Otro empleo no pleno | Insuficiencia de horas o de ingresos sin deseo de trabajar más | Ocupado |
| 5 | Empleo no remunerado | Ocupado sin ingreso laboral el mes anterior | Ocupado |
| 6 | Empleo no clasificado | Ocupado con información insuficiente para clasificarlo | Ocupado |
| 7 | Desempleo abierto | Sin empleo, busca y está disponible | Desocupado |
| 8 | Desempleo oculto | Sin empleo, no busca por razones específicas, está disponible | Desocupado |
| 9 | Población económicamente inactiva (PEI) | Fuera de la fuerza de trabajo | PEI |

Agregados usados: ocupados = 1 a 6; PEA = 1 a 8; PET = 1 a 9 (15 años o más).

Advertencia: el documento metodológico es de 2015 (sintaxis de 2014, SBU de 340 USD). Que se aplique sin cambios a la base de 2026 no está verificado; lo que sí se verificó es que los indicadores agregados reproducen cifras publicadas (informalidad 53,5 %).

## 3. Ingreso y horas

| Variable | Descripción | Estado |
|---|---|---|
| `ingrl` | Ingreso laboral del mes anterior (ocupación principal más secundaria), asumido en USD mensuales. Independientes: neto de gastos. Dependientes: incluye impuestos y aportes. Los valores −1 y 999999 se recodifican como faltantes. | Documentado; unidad asumida |
| `p24` | Horas efectivamente trabajadas la semana de referencia. | Documentado |
| `p51a`, `p51b`, `p51c` | Horas habituales de trabajo (principal, secundaria, otras). La sintaxis oficial suma todas las `p51*`; 999 es faltante. | Documentado |
| `horas_total` (derivada) | `p51a + p51b + p51c`, con faltantes de `p51b` y `p51c` tratados como 0. | Verificado |

Umbral del SBU en esta base: en empleo adecuado el ingreso mínimo es 470 USD, el 0,0 % está por debajo de 470 y el 3,49 % por debajo de 482 (SBU 2026). El máximo en subempleo por ingresos es 480 USD.

- **Hipótesis:** el INEC aplicó el SBU de 2025 (470 USD) al ingreso del mes anterior. Explica el 3,49 % bajo 482.
- **Sin explicar:** el máximo de 480 en subempleo por ingresos es algo superior a 470; podría haber umbrales mixtos según el mes de referencia. No lo verifiqué.

Cobertura de ingreso: 35.302 de 39.920 ocupados (88,4 %) tienen `ingrl` válido.

## 4. Demografía y educación

| Variable | Descripción | Estado |
|---|---|---|
| `p02` | Sexo (derivada: `sexo`). | Verificado |
| `p03` | Edad en años; 99 se recodifica como faltante. | Verificado |
| `p15` | Nivel de instrucción más alto aprobado. Sus nulos coinciden con los de `nnivins` (edades 0 a 4). | Verificado |
| `nnivins` | Nivel de instrucción (agrupado). | Verificado |
| `p10a`, `p10b` | Autoidentificación étnica y detalle. Se agrupa como Indígena, Montuvio, Afrodescendiente, Blanco y Mestizo; "Otra" (n = 17) se excluye de los gráficos. | Verificado |

## 5. Ocupación

| Variable | Descripción | Estado |
|---|---|---|
| `secemp` | Sector de empleo. Informal si `secemp == 2`, sobre ocupados. | Verificado (53,5 %) |
| `grupo1` | Grupo de ocupación. | Documentado |
| `rama1` | Rama de actividad económica. | Documentado |

## 6. Variables derivadas (`src/features.py`)

| Variable | Construcción |
|---|---|
| `anios_estudio` | Mapeo de `p15` a años: `{4:0, 5:0, 6:6, 7:10, 8:13, 9:13, 10:17}` |
| `exper` | `p03 − anios_estudio − 6`, mínimo 0 (experiencia potencial) |
| `grupo_edad` | 15-24, 25-34, 35-44, 45-54, 55-64, 65+ |
| `informal` | 1 si `secemp == 2`, 0 si no, faltante fuera de ocupados |
| `zona`, `sexo`, `etnia`, `dominio_nombre` | Etiquetas legibles de `area`, `p02`, `p10a` y `dominio` |

## 7. Pendiente

- Catálogo de códigos de `ciudad` (provincias): no resuelto; impide análisis provincial.
- Confirmar con el INEC si el umbral de 470 USD aplica a toda la base y por qué el máximo de subempleo por ingresos es 480.
- Diferencia de una décima en participación global (63,7 % frente a 63,8 %): causa desconocida.
