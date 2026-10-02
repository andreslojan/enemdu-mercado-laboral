import numpy as np
import pandas as pd

# Años acumulados antes de empezar cada nivel (supuestos documentados en el README)
BASE_ANIOS = {4: 0, 5: 0, 6: 6, 7: 10, 8: 13, 9: 13, 10: 17}


def anios_estudio(df):
    """Años de estudio a partir de nivel (p10a) y año aprobado (p10b)."""
    base = df["p10a"].map(BASE_ANIOS)
    anios = np.where(df["p10a"].isin([1, 2, 3]), 0, base + df["p10b"])
    return pd.Series(anios, index=df.index)


def agregar_variables(df):
    df = df.copy()
    ocupado = df["condact"].between(1, 6)

    df["sexo"] = df["p02"].map({1: "Hombre", 2: "Mujer"})
    df["zona"] = df["area"].map({1: "Urbana", 2: "Rural"})
    df["dominio_nombre"] = df["dominio"].map(
        {1: "Quito", 2: "Guayaquil", 3: "Cuenca", 4: "Machala", 5: "Ambato", 6: "Resto país"})
    df["etnia"] = df["p15"].map(
        {1: "Indígena", 2: "Afroecuatoriano", 3: "Negro", 4: "Mulato",
         5: "Montuvio", 6: "Mestizo", 7: "Blanco", 8: "Otra"})

    df["anios_estudio"] = anios_estudio(df)
    df["exper"] = (df["p03"] - df["anios_estudio"] - 6).clip(lower=0)   # experiencia potencial
    df["grupo_edad"] = pd.cut(df["p03"], bins=[14, 24, 34, 44, 54, 64, 120],
                              labels=["15-24", "25-34", "35-44", "45-54", "55-64", "65+"])
    df["informal"] = np.where(ocupado, (df["secemp"] == 2).astype(int), np.nan)
    return df