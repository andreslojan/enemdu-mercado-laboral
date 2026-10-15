# Pruebas

import numpy as np
import pandas as pd
import pytest
import unicodedata

from src.data import tasa_ponderada, mediana_ponderada, indicadores_laborales
from src.features import anios_estudio


def test_tasa_ponderada():
    df = pd.DataFrame({"fexp": [1, 3, 2, 4],
                       "a": [True, True, False, False],
                       "b": [True, True, True, False]})
    assert tasa_ponderada(df, df["a"], df["b"]) == pytest.approx(100 * 4 / 6)


def test_mediana_ponderada():
    v = pd.Series([10, 20, 30])
    assert mediana_ponderada(v, pd.Series([1, 1, 1])) == 20
    assert mediana_ponderada(v, pd.Series([1, 1, 10])) == 30
    assert mediana_ponderada(pd.Series([30, 10, 20]), pd.Series([10, 1, 1])) == 30


def _sin_tildes(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def test_indicadores_laborales():
    df = pd.DataFrame({"condact": [0, 1, 2, 4, 7, 9], "fexp": [1] * 6})
    r = {_sin_tildes(k): v for k, v in indicadores_laborales(df).items()}
    assert r["participacion global"] == pytest.approx(80)
    assert r["empleo adecuado"] == pytest.approx(25)
    assert r["subempleo"] == pytest.approx(25)
    assert r["desempleo"] == pytest.approx(25)


def test_anios_estudio():
    df = pd.DataFrame({"p10a": [1, 4, 6, 7, 9, 10], "p10b": [np.nan, 6, 6, 3, 4, 2]})
    assert anios_estudio(df).tolist() == [0, 6, 12, 13, 17, 19]