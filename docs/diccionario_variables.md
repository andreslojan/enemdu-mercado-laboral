# Diccionario de variables: ENEMDU, I Trimestre 2026

**Fuente:** INEC, ENEMDU, base de personas (`enemdu_persona_2026_l_trimestre.sav`): 82.894 registros y 143 columnas, de las cuales se usan 22.
**Regla general:** todo indicador se pondera con `fexp`.
**Estados:** Confirmada, Supuesto, Pendiente.

## 1. Variables originales

| Variable | Descripción (etiqueta del .sav) | Universo | Códigos / valores | Tratamiento | Estado |
|---|---|---|---|---|---|
| `fexp` | Factor de expansión | Todos | Numérico; suma = 19.026.779 | Pondera todo | Confirmada: reproduce cifras del INEC. El diccionario del INEC solo dice "factor de expansión" |
| `condact` | Condición de actividad | Todos | 0 Menores de 15; 1 Empleo adecuado/pleno; 2 Subempleo por insuficiencia de tiempo; 3 Subempleo por insuficiencia de ingresos; 4 Otro empleo no pleno; 5 Empleo no remunerado; 6 Empleo no clasificado; 7 Desempleo abierto; 8 Desempleo oculto; 9 PEI | Ocupados = 1 a 6; PEA = 1 a 8; PET = 1 a 9 | Confirmada |
| `ingrl` | Ingreso laboral | Ocupados | -1 "gasta más de lo que gana"; 999999 "no informa"; resto en USD | -1 y 999999 pasan a NaN; el análisis usa `ingrl > 0` | Supuesto: mensual y en USD. No hay cifra oficial para contrastar. Plausible frente al SBU 2026 (USD 482) y consistente con `condact` |
| `p02` | Sexo | Todos | 1 Hombre; 2 Mujer | Se mapea a `sexo` | Confirmada |
| `p03` | Edad | Todos | Años; 98 = "98 y más"; 99 = "no informa" | 99 pasa a NaN (en esta base no aparece) | Confirmada |
| `area` | Área | Todos | 1 Urbana; 2 Rural | Se mapea a `zona` | Confirmada |
| `dominio` | Dominios | Todos | 1 Quito; 2 Guayaquil; 3 Cuenca; 4 Machala; 5 Ambato; 6 Resto país | Se mapea a `dominio_nombre` | Confirmada: 20 de 20 indicadores coinciden con el INEC |
| `ciudad` | Ciudad | Todos | Código de 5 o 6 dígitos (587 distintos), sin etiquetas | Prefijo de 2 dígitos (tras `zfill(6)`) = posible provincia | Experimental: da 24 prefijos, pero `fexp` no reproduce la población provincial |
| `conglomerado` | Conglomerado | Todos | Prefijos 00 a 54 y 90 | No se usa | No sirve como provincia |
| `upm` | Unidad Primaria de Muestreo | Todos | Sin explorar | Para errores estándar agrupados (Mincer) | Pendiente: revisar valores |
| `estrato` | Estratos | Todos | Sin etiquetas | Diseño muestral | Pendiente: revisar valores |
| `p10a` | Nivel de instrucción | Todos menos 4.137 nulos | 1 Ninguno; 2 Centro de alfabetización; 3 Jardín de infantes (sin casos); 4 Primaria; 5 Educación Básica; 6 Secundaria; 7 Educación Media; 8 Superior no universitario; 9 Superior universitario; 10 Postgrado | Base de `anios_estudio` | Confirmada. Universo de los nulos: ver pendientes |
| `p10b` | Año aprobado | 76.439 con dato (sin dato: 4.137 nulos de `p10a` + 2.318 "Ninguno") | Sin etiquetas. Rango por nivel: Alfabetización 1 a 7; Primaria 1 a 6; Básica 0 a 10; Secundaria 1 a 6; Media 1 a 3; Superior no univ. 1 a 3; Universitario 1 a 8; Postgrado 1 a 5 | Base de `anios_estudio` | Confirmada |
| `nnivins` | Nivel de instrucción (agrupado) | Mismos 4.137 nulos que `p10a` | 1 Ninguno; 2 Centro de alfabetización; 3 Educación Básica; 4 Educación Media/Bachillerato; 5 Superior | Categórica en modelos | Confirmada |
| `p15` | Como se considera (autoidentificación étnica) | Por confirmar | 1 Indígena; 2 Afroecuatoriano; 3 Negro; 4 Mulato; 5 Montuvio; 6 Mestizo; 7 Blanco; 8 Otra | Se mapea a `etnia` | Códigos confirmados; universo pendiente |
| `secemp` | Sectores de los empleados | Ocupados (verificado: no nulo = `condact` 1 a 6) | 1 Formal; 2 Informal; 3 Empleo doméstico; 4 No clasificados | `informal` = (`secemp` == 2) | Confirmada: 53,5% coincide con el boletín |
| `grupo1` | Grupo de ocupación CIUO-08 | Ocupados | 1 a 10; 99 No especificado | Sin transformar | Confirmada (etiquetas) |
| `rama1` | Rama de actividad CIIU 4.1 | Ocupados | 1 a 22 (A a U; 22 No especificado) | Sin transformar | Confirmada (etiquetas) |
| `p24` | Horas de trabajo en la semana anterior | Por confirmar | Numérico | Revisar códigos especiales | Pendiente |
| `p51a` | Horas de trabajo principal | Por confirmar | Numérico | Revisar códigos especiales | Pendiente |
| `p51b` | Horas de trabajo secundario | Por confirmar | Numérico | Revisar códigos especiales | Pendiente |
| `p51c` | Horas de otros trabajos | Por confirmar | Numérico | Revisar códigos especiales | Pendiente |

## 2. Variables derivadas (`src/features.py`)

| Variable | Definición | Notas |
|---|---|---|
| `sexo`, `zona`, `dominio_nombre`, `etnia` | Etiquetas de texto de `p02`, `area`, `dominio`, `p15` | Si se agrupan etnias (por ejemplo, afrodescendientes), declararlo |
| `anios_estudio` | Ninguno, alfabetización y jardín = 0. Primaria y Básica = `p10b`. Secundaria = 6 + `p10b`. Media = 10 + `p10b`. Superior (no univ. y univ.) = 13 + `p10b`. Postgrado = 17 + `p10b` | Convención propia, no oficial. Mezcla sistema educativo antiguo y actual (un año de diferencia) |
| `exper` | `p03 - anios_estudio - 6`, mínimo 0 | Experiencia potencial. Llega a 92 por `p03` = 98; en el Mincer se restringe la edad |
| `grupo_edad` | 15-24, 25-34, 35-44, 45-54, 55-64, 65+ | Solo para edades de 15 en adelante |
| `informal` | 1 si `secemp` == 2; 0 si es ocupado y no informal; NaN si no es ocupado | Validada contra el boletín |

## 3. Decisiones de limpieza

- `ingrl` = -1 o 999999 pasa a NaN.
- `p03` = 99 pasa a NaN (no hay casos en esta base).
- `ciudad`: no usar para análisis provincial en este trimestre.

## 4. Cómo mantener este archivo

Al agregar una variable a `COLUMNAS` o a `features.py`, agregar su fila el mismo día. Cambiar el estado solo cuando haya evidencia.