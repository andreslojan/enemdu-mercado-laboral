# Modulo de carga

from pathlib import Path
import pandas as pd
import numpy as np
import pyreadstat

RAIZ = Path(__file__).resolve().parents[1]
RUTA_SAV = RAIZ / "data" / "raw" / "spss" / "enemdu_persona_2026_l_trimestre.sav"

COLUMNAS = ["area", "ciudad", "conglomerado", "dominio", "estrato", "upm",
            "p02", "p03", "p10a", "p10b", "p15", "condact", "fexp",
            "ingrl", "secemp", "grupo1", "rama1", "nnivins",
            "p24", "p51a", "p51b", "p51c"]

def cargar_enemdu(ruta=RUTA_SAV, columnas=COLUMNAS):
    """Carga solo las columnas necesarias y limpia los codigos especiales."""
    df, _ = pyreadstat.read_sav(ruta, usecols=columnas)
    df.columns = df.columns.str.lower()

    df.loc[df["p03"] == 99, "p03"] = np.nan                   # edad: no informa 
    df.loc[df["ingrl"].isin([-1, 999999]), "ingrl"] = np.nan  #ingreso: codigos especiales
    return df


def tasa_ponderada(df, mask_num, mask_den, peso="fexp"):
    """Porcentaje ponderado: suma de pesos del numerador / suma de pesos del denominador."""
    return 100 * df.loc[mask_num, peso].sum() / df.loc[mask_den, peso].sum()


def indicadores_laborales(df):
    c = df["condact"]
    pet = c.between(1, 9)  # Población en edad de trabajar (15+)
    pea = c.between(1, 8)  # Población económicamente activa
    return {
        "Participacion global": tasa_ponderada(df, pea, pet),
        "Empleo adecuado": tasa_ponderada(df, c == 1, pea),
        "Subempleo": tasa_ponderada(df, c.isin([2, 3]), pea),
        "Desempleo": tasa_ponderada(df, c.isin([7, 8]), pea),
    }