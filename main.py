import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

def read_data(file_paths):
    """
    Lee los archivos CSV y devuelve un diccionario de DataFrames.
    """
    dataframes = {}
    for key, path in file_paths.items():
        dataframes[key] = pd.read_csv(path)
    return dataframes


print("Leyendo datos...")
print(read_data("/processed_data/bc-mx.csv"))