# carga_datos.py
import pandas as pd
from ucimlrepo import fetch_ucirepo

def cargar_datos_bicicletas():
    """
    Carga el conjunto de datos de uso compartido de bicicletas desde ucimlrepo y lo devuelve como un DataFrame.
    """
    dataset = fetch_ucirepo(id=275)
    caracteristicas = dataset.data.features
    objetivo = dataset.data.targets
    df = pd.concat([caracteristicas, objetivo], axis=1)
    return df
