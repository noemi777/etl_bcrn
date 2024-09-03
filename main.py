import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def read_data(file_paths):
    """
    Lee los archivos CSV y devuelve un diccionario de DataFrames.
    """
    dataframes = {}
    for key, path in file_paths.items():
        dataframes[key] = pd.read_csv(path)
    return dataframes


def transform_data(df):
    """
    Realiza la transformación de datos sobre un DataFrame.
    """
    
    diccionario_columnas = {
        "State": "Estado",
        "Value Export": "Valor de Exportación",
        "Value Import": "Valor de Importación",
        "Value Delta": "Valor Delta",
    }
    df = df.rename(columns=diccionario_columnas)
    df = df.dropna()

    return df

def exploratory_analysis(df, output_dir):
    """
    Realiza un análisis exploratorio de datos sobre el DataFrame combinado y guarda los gráficos en el directorio especificado.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Añadir líneas divisorias y saltos de línea en los prints
    print("\n" + "="*40 + "\n")
    print(df.info())
    print("\n" + "="*40 + "\n")
    print(df.describe())
    print("\n" + "="*40 + "\n")
    print(df.head())

    # Gráfico de barras para el valor de exportación por estado
    plt.figure(figsize=(12, 8))
    plt.bar(df["Estado"], df["Valor de Importación"], color='skyblue')
    plt.xlabel("Estado")
    plt.ylabel("Valor de Importación")
    plt.title("Valor de Importación por Estado")
    plt.xticks(rotation=90)  # Rotate the x-axis labels for better readability
    plt.tight_layout()
    # Guardar el gráfico
    plt.savefig(os.path.join(output_dir, "import_value_by_state.png"))

    # Gráfico de barras para el valor de Exportación por estado
    plt.figure(figsize=(12, 8))
    plt.bar(df["Estado"], df["Valor de Exportación"], color='lightcoral')
    plt.xlabel("Estado")    
    plt.ylabel("Valor de Exportación")
    plt.title("Valor de Exportación por Estado")
    plt.xticks(rotation=90)
    plt.tight_layout()
    # Guardar el gráfico
    plt.savefig(os.path.join(output_dir, "export_value_by_state.png"))

    # Gráfico de barras para el valor Delta por estado
    plt.figure(figsize=(12, 8))
    plt.bar(df["Estado"], df["Valor Delta"], color='lightgreen')
    plt.xlabel("Estado")
    plt.ylabel("Valor Delta")
    plt.title("Valor Delta por Estado")
    plt.xticks(rotation=90)
    plt.tight_layout()
    # Guardar el gráfico
    plt.savefig(os.path.join(output_dir, "delta_value_by_state.png"))

    # Gráfico de dispersión para el valor de exportación vs. importación
    plt.figure(figsize=(12, 8))
    plt.scatter(df["Valor de Exportación"], df["Valor de Importación"], color='orange')
    plt.xlabel("Valor de Exportación")
    plt.ylabel("Valor de Importación")
    plt.title("Valor de Exportación vs. Valor de Importación")
    plt.tight_layout()
    # Guardar el gráfico
    plt.savefig(os.path.join(output_dir, "export_vs_import_value.png"))

    # Histograma para el valor de exportación
    plt.figure(figsize=(12, 8))
    plt.hist(df["Valor de Exportación"], bins=20, color='lightblue')
    plt.xlabel("Valor de Exportación")
    plt.ylabel("Frecuencia")
    plt.title("Histograma del Valor de Exportación")
    plt.tight_layout()
    # Guardar el gráfico
    plt.savefig(os.path.join(output_dir, "export_value_histogram.png"))
    


def load_processed_data(df, output_path):
    """
    Guarda el DataFrame procesado en un archivo CSV.
    """
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    df.to_csv(output_path, index=False)

# Rutas de archivos
file_paths = {
    "bc-mx": "processed_data/bc-mx-ef.csv",
}

dataframes = read_data(file_paths)
# Transformación de datos
transformed_dataframes = transform_data(dataframes["bc-mx"])
print(transformed_dataframes)
# Análisis exploratorio de datos
print(exploratory_analysis(transformed_dataframes, "output"))