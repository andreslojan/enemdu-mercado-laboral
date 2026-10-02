# Diccionario de variables: ENEMDU, I Trimestre 2026

**Fuente:** INEC, ENEMDU, base de personas (`enemdu_persona_2026_l_trimestre.sav`): 82.894 registros y 143 columnas. Se cargan 22.
**Regla general:** todo indicador se pondera con `fexp`.
**Estados:** *Confirmada* (validada con cifras oficiales o coherencia interna), *Supuesto* (razonable, no verificado), *Pendiente*, *Experimental*.

## 1. Variables originales

| Variable | Descripción (etiqueta del .sav) | Universo | Códigos / valores | Tratamiento | Estado |
|---|---|---|---|---|---|
| `fexp` | Factor de expansión | Todos | Numérico; suma = 19.026.779 | Pondera todo | Confirmada: reproduce las cifras del INEC. El diccionario del INEC solo dice "factor de expansión" |
| `condact` | Condición de actividad | Todos | 0 Menores de 15; 1 Empleo adecuado/pleno; 2 Subempleo por insuficiencia de tiempo; 3 Subempleo por insuficiencia de ingresos; 4 Otro empleo no pleno; 5 Empleo no remunerado; 6 Empleo no clasificado; 7 Desempleo abierto; 8 Desempleo oculto; 9 Población económicamente inactiva | Ocupados = 1 a 6; PEA = 1 a 8; PET = 1 a 9 | Confirmada |
| `ingrl` | Ingreso laboral | Ocupados (39.920) | -1 "gasta más de lo que gana" (380); 999999 "no informa" (123); vacío (3.570); 0 (545); resto en USD (35.302) | -1 y 999999 pasan a NaN. El análisis usa ocupados con `ingrl > 0` | Supuesto: mensual y en USD. Sin cifra oficial para contrastar. Plausible frente al SBU 2026 (USD 482). Ver sección 4 |
| `p02` | Sexo | Todos | 1 Hombre; 2 Mujer | Se mapea a `sexo` | Confirmada |
| `p03` | Edad | Todos | Años; 98 = "98 y más"; 99 = "no informa" | 99 pasa a NaN (no hay casos en esta base) | Confirmada |
| `area` | Área | Todos | 1 Urbana; 2 Rural | Se mapea a `zona` | Confirmada |
| `dominio` | Dominios | Todos | 1 Quito; 2 Guayaquil; 3 Cuenca; 4 Machala; 5 Ambato; 6 Resto país | Se mapea a `dominio_nombre` | Confirmada: 20 de 20 indicadores coinciden con el INEC |
| `ciudad` | Ciudad | Todos | Código de 5 dígitos (39.782 casos) o 6 dígitos (43.112); 587 valores distintos; sin etiquetas | Prefijo de 2 dígitos (tras `zfill(6)`) = posible provincia | Experimental: da 24 prefijos, pero `fexp` no reproduce la población provincial |
| `conglomerado` | Conglomerado | Todos | Prefijos 00 a 54 y 90 | No se usa | No sirve como provincia |
| `upm` | Unidad Primaria de Muestreo | Todos | 3.855 valores distintos | Errores estándar agrupados en el modelo de ingresos | Confirmada (existe); estructura pendiente |
| `estrato` | Estratos | Todos | 150 valores distintos; sin etiquetas | Diseño muestral | Pendiente: relación con `upm` |
| `p10a` | Nivel de instrucción | 5 años y más (los 4.137 nulos tienen de 0 a 4 años) | 1 Ninguno; 2 Centro de alfabetización; 3 Jardín de infantes (sin casos); 4 Primaria; 5 Educación Básica; 6 Secundaria; 7 Educación Media; 8 Superior no universitario; 9 Superior universitario; 10 Postgrado | Base de `anios_estudio` | Confirmada |
| `p10b` | Año aprobado | Con dato: 76.439. Sin dato: 6.455 = 4.137 (0 a 4 años) + 2.318 ("Ninguno") | Sin etiquetas. Rango por nivel: Alfabetización 1 a 7; Primaria 1 a 6; Básica 0 a 10; Secundaria 1 a 6; Media 1 a 3; Superior no univ. 1 a 3; Universitario 1 a 8; Postgrado 1 a 5 | Base de `anios_estudio` | Confirmada |
| `nnivins` | Nivel de instrucción (agrupado) | 5 años y más (mismos 4.137 nulos que `p10a`) | 1 Ninguno; 2 Centro de alfabetización; 3 Educación Básica; 4 Educación Media/Bachillerato; 5 Superior | Categórica en modelos | Confirmada |
| `p15` | Como se considera (autoidentificación étnica) | 4.137 nulos, igual cantidad que `p10a`; falta verificar que sean las mismas personas | 1 Indígena; 2 Afroecuatoriano; 3 Negro; 4 Mulato; 5 Montuvio; 6 Mestizo; 7 Blanco; 8 Otra | Se mapea a `etnia` | Códigos confirmados; universo pendiente |
| `secemp` | Sectores de los empleados | Ocupados (verificado: no nulo coincide con `condact` 1 a 6) | 1 Formal; 2 Informal; 3 Empleo doméstico; 4 No clasificados | `informal` = (`secemp` == 2) | Confirmada: 53,5% coincide con el boletín |
| `grupo1` | Grupo de ocupación CIUO-08 | Ocupados | 1 a 10; 99 No especificado | Sin transformar | Confirmada (etiquetas) |
| `rama1` | Rama de actividad CIIU 4.1 | Ocupados | 1 a 22 (A a U; 22 No especificado) | Sin transformar | Confirmada (etiquetas) |
| `p24` | Horas de trabajo en la semana anterior | Dato en todos los ocupados; también en 378 no ocupados | Numérico; rango 1 a 120; mediana 40 | Sin transformar | Confirmada (descriptivo); definición exacta pendiente |
| `p51a` | Horas de trabajo principal | Dato en todos los ocupados | Numérico; rango 1 a 120; media 35,1; mediana 40 | Sin transformar | Pendiente: ¿habituales o efectivas? |
| `p51b` | Horas de trabajo secundario | Unos 2.400 ocupados (6%) con dato | Numérico; rango 1 a 45; mediana 10 | Vacío se interpreta como "sin segundo trabajo" | Supuesto |
| `p51c` | Horas de otros trabajos | Unos 2.400 ocupados con dato | Numérico; rango 0 a 20; casi siempre 0 | Vacío se interpreta como "sin otros trabajos" | Supuesto |

## 2. Variables derivadas (`src/features.py`)

| Variable | Definición | Notas |
|---|---|---|
| `sexo`, `zona`, `dominio_nombre`, `etnia` | Etiquetas de texto de `p02`, `area`, `dominio`, `p15` | Si se agrupan etnias (por ejemplo, afrodescendientes), declararlo |
| `anios_estudio` | Ninguno, alfabetización y jardín = 0. Primaria y Básica = `p10b`. Secundaria = 6 + `p10b`. Media = 10 + `p10b`. Superior (no univ. y univ.) = 13 + `p10b`. Postgrado = 17 + `p10b` | Convención propia, no oficial. Mezcla el sistema educativo antiguo y el actual (un año de diferencia). Sin valor para menores de 5 años |
| `exper` | `p03 - anios_estudio - 6`, mínimo 0 | Experiencia potencial. Llega a 92 por `p03` = 98; en el modelo de ingresos se restringe la edad |
| `grupo_edad` | 15-24, 25-34, 35-44, 45-54, 55-64, 65+ | Solo para edades de 15 en adelante |
| `informal` | 1 si `secemp` == 2; 0 si es ocupado y no informal; NaN si no es ocupado | Validada contra el boletín |

## 3. Decisiones de limpieza

- `ingrl` = -1 o 999999 pasa a NaN.
- El análisis de ingresos usa ocupados con `ingrl > 0`: 35.302 de 39.920 (88,4%).
- `p03` = 99 pasa a NaN (no hay casos en esta base).
- `ciudad`: no usar para análisis provincial en este trimestre.

## 4. Cobertura del ingreso laboral (`ingrl`)

| `condact` | Ocupados | Vacío o código especial (NaN) | Ingreso = 0 | Con ingreso > 0 |
|---|---|---|---|---|
| 1 Empleo adecuado | 17.135 | 0 | 0 | 17.135 |
| 2 Subempleo por tiempo | 6.541 | 592 | 126 | 5.823 |
| 3 Subempleo por ingresos | 406 | 0 | 13 | 393 |
| 4 Otro empleo no pleno | 12.689 | 332 | 406 | 11.951 |
| 5 Empleo no remunerado | 3.030 | 3.030 | 0 | 0 |
| 6 Empleo no clasificado | 119 | 119 | 0 | 0 |
| **Total** | **39.920** | **4.073** | **545** | **35.302** |

- Los no remunerados y los no clasificados (3.149 personas) quedan fuera del análisis de ingresos porque no tienen ingreso. Eso es un sesgo de selección.
- Verificación de plausibilidad con el SBU 2026 (USD 482, según el Ministerio de Trabajo):

| `condact` | Mediana (USD) | % bajo el SBU |
|---|---|---|
| 1 Empleo adecuado | 640 | 3,5 |
| 2 Subempleo por tiempo | 200 | 94,0 |
| 3 Subempleo por ingresos | 291 | 100,0 |
| 4 Otro empleo no pleno | 234 | 99,9 |

- El umbral esperado por cada categoría es de memoria. Falta confirmarlo en la página "Metodología de empleo según condición de actividad" del INEC. Los casos que no encajan (3,5% y 6,0%) no se han podido explicar.

## 5. Horas de trabajo

- `p24` coincide con `p51a` en 79,6% de los ocupados, y con `p51a` + `p51b` + `p51c` en 84,8%. Sugiere que `p24` incluye todos los trabajos (inferencia, no confirmada).
- Suma de las tres variables `p51`: media 36,1; mediana 40; percentil 99 = 70; máximo 129. 25 casos superan las 84 horas y 5 superan las 100.

## 6. Pendientes

1. Confirmar si `p51a` son horas habituales o efectivas.
2. Decidir el tratamiento de las horas extremas en el modelo de ingresos.
3. Confirmar los umbrales de `condact` frente al SBU en la metodología del INEC.
4. Verificar que los nulos de `p15` son las mismas personas que los de `nnivins`.
5. Contrastar los prefijos de `ciudad` con el catálogo oficial de provincias.
6. Revisar cómo se relacionan `upm` y `estrato`.
7. Agregar `horas_total` a `features.py` cuando se decida cómo tratar los extremos.

## 7. Cómo mantener este archivo

Cada vez que se agregue una variable a `COLUMNAS` o a `features.py`, agregar su fila el mismo día. Cambiar un estado solo cuando haya evidencia.