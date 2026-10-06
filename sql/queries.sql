-- name: q1_nacional
-- Indicadores laborales nacionales ponderados
WITH s AS (
  SELECT
    SUM(CASE WHEN condact BETWEEN 1 AND 9 THEN fexp END) AS pet,
    SUM(CASE WHEN condact BETWEEN 1 AND 8 THEN fexp END) AS pea,
    SUM(CASE WHEN condact = 1 THEN fexp END)             AS adecuado,
    SUM(CASE WHEN condact IN (2, 3) THEN fexp END)       AS subempleo,
    SUM(CASE WHEN condact IN (7, 8) THEN fexp END)       AS desempleo
  FROM personas
)
SELECT ROUND(100.0 * pea / pet, 1)       AS participacion,
       ROUND(100.0 * adecuado / pea, 1)  AS empleo_adecuado,
       ROUND(100.0 * subempleo / pea, 1) AS subempleo,
       ROUND(100.0 * desempleo / pea, 1) AS desempleo
FROM s;

-- name: q2_dominios
-- Los mismos indicadores por dominio (cinco ciudades principales)
WITH s AS (
  SELECT dominio_nombre,
    SUM(CASE WHEN condact BETWEEN 1 AND 9 THEN fexp END) AS pet,
    SUM(CASE WHEN condact BETWEEN 1 AND 8 THEN fexp END) AS pea,
    SUM(CASE WHEN condact = 1 THEN fexp END)             AS adecuado,
    SUM(CASE WHEN condact IN (2, 3) THEN fexp END)       AS subempleo,
    SUM(CASE WHEN condact IN (7, 8) THEN fexp END)       AS desempleo
  FROM personas
  WHERE dominio BETWEEN 1 AND 5
  GROUP BY dominio_nombre
)
SELECT dominio_nombre,
       ROUND(100.0 * pea / pet, 1)       AS participacion,
       ROUND(100.0 * adecuado / pea, 1)  AS empleo_adecuado,
       ROUND(100.0 * subempleo / pea, 1) AS subempleo,
       ROUND(100.0 * desempleo / pea, 1) AS desempleo
FROM s
ORDER BY dominio_nombre;

-- name: q3_informalidad_zona_sexo
-- Informalidad (sector informal sobre ocupados) por zona y sexo
SELECT zona, sexo,
       ROUND(100.0 * SUM(CASE WHEN secemp = 2 THEN fexp END) / SUM(fexp), 1) AS pct_informal
FROM personas
WHERE condact BETWEEN 1 AND 6
GROUP BY zona, sexo
ORDER BY zona DESC, sexo;

-- name: q4_pareto_rama
-- Peso de cada rama en la informalidad total, con acumulado
WITH por_rama AS (
  SELECT r.nombre AS rama,
         SUM(p.fexp) AS ocupados,
         COALESCE(SUM(CASE WHEN p.secemp = 2 THEN p.fexp END), 0) AS informales
  FROM personas p
  JOIN dim_rama r ON r.codigo = p.rama1
  WHERE p.condact BETWEEN 1 AND 6
  GROUP BY r.nombre
)
SELECT rama,
       ROUND(100.0 * informales / ocupados, 1) AS pct_informal,
       ROUND(100.0 * informales / SUM(informales) OVER (), 1) AS pct_de_los_informales,
       ROUND(100.0 * SUM(informales) OVER (ORDER BY informales DESC) / SUM(informales) OVER (), 1) AS acumulado
FROM por_rama
ORDER BY informales DESC;

-- name: q5_cambio_por_edad
-- Empleo adecuado por grupo de edad y cambio frente al grupo anterior (LAG)
WITH edad AS (
  SELECT grupo_edad,
         100.0 * SUM(CASE WHEN condact = 1 THEN fexp END) / SUM(fexp) AS pct_adecuado
  FROM personas
  WHERE condact BETWEEN 1 AND 8 AND grupo_edad IS NOT NULL
  GROUP BY grupo_edad
)
SELECT grupo_edad,
       ROUND(pct_adecuado, 1) AS pct_adecuado,
       ROUND(pct_adecuado - LAG(pct_adecuado) OVER (ORDER BY grupo_edad), 1) AS cambio_vs_anterior
FROM edad
ORDER BY grupo_edad;

-- name: q6_mediana_ponderada
-- Mediana ponderada del ingreso laboral por sexo, con suma acumulada de pesos
WITH base AS (
  SELECT sexo, ingrl, fexp,
         SUM(fexp) OVER (PARTITION BY sexo ORDER BY ingrl) AS acum,
         SUM(fexp) OVER (PARTITION BY sexo) AS total
  FROM personas
  WHERE condact BETWEEN 1 AND 6 AND ingrl > 0
)
SELECT sexo, MIN(ingrl) AS mediana_ponderada
FROM base
WHERE acum >= total / 2.0
GROUP BY sexo;