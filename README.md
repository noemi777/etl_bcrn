 ⚙️ ETL para Balanza Comercial de Reactores Nucleares 🚀

Esto es un etl relacioado a datos provenientes de https://www.economia.gob.mx/datamexico/es/profile/product/nuclear-reactors-boilers-machinery-etc?sourceTradeBalance=seOption, en donde los datos reflejan el intercambio comercial de reactores nucleares, calderas, maquinarias, etc., de México con otros países.


## 🏗️ Arquitectura

El flujo ETL se compone de los siguientes pasos:

1. **🗂️ Extracción**: Se obtienen datos de diversas fuentes (APIs, archivos CSV, bases de datos).
2. **🔄 Transformación**: Se procesan los datos para corregir errores, convertir tipos de datos y aplicar reglas de negocio.
3. **📥 Carga**: Los datos transformados se almacenan en una base de datos SQL para análisis y visualización. (Pendiente)


## Requerimientos

- Matplotlib
- [Pandas](https://pandas.pydata.org/)

- ## ⚙️ Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/usuario/etl-reactores-nucleares.git
    cd etl-reactores-nucleares
    ```

2. Crea un entorno virtual y activa el entorno:

    ```bash
    python -m venv venv
    source venv/bin/activate   # En Windows usa: venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Uso

1. **Ejecutar ETL manualmente**:

    ```bash
    python main.py
    ```

