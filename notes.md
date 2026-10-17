# Notas del proyecto: hipótesis e interpretación

Este documento separa lo que los datos muestran de lo que yo supongo. Cada hipótesis dice qué observé, qué creo que lo explica, qué lo respalda y qué haría falta para comprobarla. Ninguna se interpreta como causal.

Estados: **Medido** = cifra calculada con los datos. **Respaldada** = los datos la apoyan, con salvedades. **Hipótesis** = explicación plausible que estos datos no prueban.

## Resumen

| # | Tema | Estado |
|---|---|---|
| 1 | Informalidad e instrucción | Hipótesis |
| 2 | Desempleo juvenil | Hipótesis |
| 3 | Empleo adecuado a los 65 años o más | Hipótesis |
| 4 | Etnia y zona | Parcialmente respaldada (cálculo aproximado) |
| 5 | Informalidad por sexo, con signo opuesto por zona | Hipótesis |
| 6 | Agricultura concentra la informalidad | Medido; falta explicarlo |
| 7 | Menor participación femenina de 15 a 24 años | Hipótesis |
| 8 | La brecha de ingresos crece al controlar educación y zona | Respaldada |
| 9 | Pico de ingresos en el SBU | Medido |
| 10 | Las mujeres trabajan menos horas y eso reduce la brecha | Respaldada de forma aproximada; las causas son hipótesis |
| 11 | Sensibilidad de la brecha a la muestra | Medido |
| 12 | Retornos no lineales por nivel educativo | Medido |

## Detalle

### 1. Informalidad e instrucción (gráficos 5 y 6)
- **Observado:** la informalidad baja de 90,0 % a 74,6 %, 48,3 % y 19,6 % al subir el nivel de instrucción; el ingreso mediano sube de 155 a 270, 430 y 663 USD.
- **Hipótesis:** los empleos formales exigen credenciales, y quienes tienen menos estudios se concentran en zonas rurales y ocupaciones elementales.
- **Por qué no está probada:** los gráficos son descriptivos y mezclan zona, ocupación y horas.
- **Para comprobarla:** un modelo de informalidad con controles por zona y ocupación (trabajo futuro).

### 2. Desempleo juvenil (gráfico 4)
- **Observado:** el desempleo es mayor entre los 15 y 24 años.
- **Hipótesis:** refleja la entrada reciente al mercado y la búsqueda del primer empleo. A edades altas el desempleo es bajo en parte porque quienes pierden el empleo dejan de buscar y salen de la PEA.
- **Para comprobarla:** series de varios períodos o datos de transiciones; con un solo trimestre no se puede.

### 3. Empleo adecuado a los 65 años o más
- **Observado:** el empleo adecuado sube hasta los 25 a 34 años y cae después de los 45, hasta 12,9 % a los 65 o más, donde domina "otro empleo no pleno".
- **Hipótesis:** a edades altas hay más trabajo independiente y agrícola, donde el empleo adecuado es menos frecuente.
- **Para comprobarla:** cruzar edad por rama y categoría de ocupación.

### 4. Etnia y zona
- **Observado:** empleo adecuado de 11,4 % en indígenas y 41,2 % en mestizos. El 87,8 % de los indígenas vive en zona rural, frente al 23,5 % de los mestizos.
- **Cálculo aproximado:** de los 29,8 puntos de diferencia, unos 16 se deberían a la composición por zona y unos 14 persistirían dentro de cada zona.
- **Salvedad:** es una aproximación, no una descomposición formal.
- **Para comprobarla:** descomposición de Oaxaca-Blinder u otro método formal.

### 5. Informalidad por sexo, con signo opuesto por zona
- **Observado:** en zona urbana las mujeres tienen menos informalidad (hombres 44,7 %, mujeres 37,2 %); en zona rural tienen más (hombres 73,5 %, mujeres 78,9 %).
- **Hipótesis:** distinta composición ocupacional de las mujeres en cada zona (por ejemplo empleo público o de servicios en ciudades, y trabajo agrícola familiar en el campo).
- **Para comprobarla:** cruzar sexo por rama y zona.

### 6. Agricultura concentra la informalidad
- **Medido:** agricultura es el 32,3 % de los ocupados, tiene 86,1 % de informalidad y explica el 51,9 % de todos los informales. Con comercio y construcción se llega al 74,6 % acumulado.
- **Falta explicarlo:** el dato es firme; las causas (trabajo familiar, autoempleo, baja cobertura de seguridad social) no se analizaron.

### 7. Menor participación femenina de 15 a 24 años
- **Hipótesis:** puede reflejar estudio, cuidados del hogar o maternidad temprana. Los datos descriptivos no distinguen entre estas razones.
- **Para comprobarla:** analizar la razón de inactividad dentro de la PEI por sexo y edad.

### 8. La brecha de ingresos crece al controlar educación y zona
- **Respaldada:** en la tabla de perfil, las mujeres tienen más educación en promedio, por lo que controlar por educación no reduce la brecha, la amplía.
- **Salvedad:** el resultado depende de la muestra (ver 11).

### 9. Pico de ingresos en el SBU
- **Medido:** el 2,5 % de los ocupados reporta un ingreso exactamente igual a 482 USD (SBU 2026).
- **Interpretación:** es consistente con empleadores que pagan el salario mínimo, pero no se comprobó; no se interpreta como evidencia de nada más.
- **Relacionado:** en empleo adecuado, el ingreso mínimo es 470 USD y ninguno está bajo 470, mientras que el 3,49 % está bajo 482. Hipótesis, no verificada oficialmente: el INEC aplicó el SBU de 2025 (470 USD). El máximo de 480 en subempleo por ingresos queda sin explicar.

### 10. Las mujeres trabajan menos horas y eso reduce la brecha
- **Respaldada de forma aproximada:** al añadir horas a M2, la brecha cae de −29,6 % a −8,7 % [−13,8; −3,4]. La cuenta aproximada encaja con la caída de 0,176 en logaritmos entre M2 y M3.
- **Hipótesis:** por qué trabajan menos horas (cuidados del hogar, trabajo a tiempo parcial) no se puede probar con estos datos.
- **Salvedad:** el efecto de la rama es una hipótesis. En tiempo completo, controlar por rama agranda la brecha (−2,5 % a −7,4 %), pero los intervalos se superponen. Es consistente con que las mujeres se concentren en ramas mejor pagadas y ganen menos que los hombres dentro de ellas, pero falta una descomposición formal.

### 11. Sensibilidad de la brecha a la muestra
- **Medido:** no existe una única brecha ajustada.

| Muestra | n | Brecha M2 | Brecha M3 |
|---|---|---|---|
| Completa | 32.258 | −29,6 % [−34,1; −24,7] | −16,1 % [−20,1; −11,8] |
| Sin 1 % extremos | 31.690 | −26,2 % [−31,1; −21,0] | −13,6 % [−17,7; −9,3] |
| Tiempo completo (35 a 48 h) | 19.720 | −2,5 % [−9,8; +5,3] | −7,4 % [−12,6; −2,0] |

### 12. Retornos no lineales por nivel educativo
- **Medido (M4, frente a Primaria o menos):** Básica +5,5 % [−4,9; 17,0], Media +21,5 % [9,0; 35,4], Superior +73,4 % [54,9; 94,2]. Superior frente a Media: +42,7 % [37,0; 48,6].
- **Lectura:** el retorno por año de estudio es relativamente estable (7,8 % a 8,9 % en M2 según la muestra), pero los saltos por nivel no son uniformes; la mayor parte del retorno aparece al llegar a educación superior.

## Preguntas de entrevista

Pregunta 1: ¿Por qué ponderas con fexp?
Porque la encuesta no da el mismo peso a todas las personas. Cada registro representa a un número distinto de habitantes, y sin fexp las cifras describirían la muestra, no el país. Todas las tasas son una razón de sumas de pesos.

Pregunta 2: ¿Cómo validaste tu trabajo?
Antes de analizar, reproduje cifras publicadas por el INEC a nivel nacional, por dominio y en informalidad (53,5 %). La participación global difiere en una décima (63,7 % frente a 63,8 %). No sé la causa y lo dejé documentado. Además, SQL reproduce pandas y las tarjetas de Power BI reproducen ambos.

Pregunta 3: ¿Por qué el logaritmo del ingreso y los errores agrupados por UPM?
El ingreso es muy asimétrico. Con el logaritmo los coeficientes se leen como diferencias porcentuales aproximadas, y los valores extremos pesan menos. Las personas de una misma UPM se parecen entre sí, así que tratarlas como independientes subestimaría la incertidumbre. Agrupar por UPM lo corrige en parte, aunque no modela el diseño muestral completo.

Pregunta 4: ¿Por qué la brecha de las mujeres cambia con los controles, y por qué no dices que sea discriminación?
La brecha pasa de −29,6 % a −16,1 % al controlar por ocupación y zona, y a −8,7 % al controlar por horas trabajadas. En tiempo completo vale −2,5 % con un intervalo que incluye el cero. Una parte grande se asocia con horas y ocupación. No puedo atribuir lo que queda a una causa, porque no observo cuidados del hogar, preferencias ni trato diferenciado. Son asociaciones, no causalidad.

Pregunta 5: ¿Por qué el dashboard guarda sumas de pesos y no porcentajes?
Una tasa de grupo es una razón de sumas, no un promedio de porcentajes. Si el usuario combina categorías con un filtro, un porcentaje precalculado daría un número incorrecto. Con numerador y denominador, la medida DAX lo recalcula bien. Además, no se publican microdatos.

Pregunta 6: ¿Por qué no usaste provincias?
La base es representativa por dominio (cinco ciudades y resto del país), no por provincia. Además, no pude validar el catálogo de códigos de ciudad. Prefiero no publicar cifras provinciales que no puedo respaldar. Para eso haría falta la base anual.

Pregunta 7: ¿Qué limitación te preocupa más?
El sesgo de selección del ingreso: solo 35.302 de 39.920 ocupados (88,4 %) reportan ingreso válido. Si quienes no lo reportan difieren sistemáticamente, las medianas y la brecha cambian. No puedo medir cuánto, y no lo corregí.

Pregunta 8: ¿Qué harías con más tiempo?
- Sumar más períodos, cuidando el quiebre metodológico de 2020 a mayo de 2021.
- Calcular errores estándar que respeten el diseño muestral completo.
- Hacer una descomposición formal de la brecha de género.
- Construir un modelo de informalidad.
- Repetir la robustez con horas efectivas (p24).
