# Proyecto de Análisis Descriptivo de Datos

Este proyecto realiza un análisis descriptivo del conjunto de datos de uso compartido de bicicletas (*Bike Sharing Dataset*). El objetivo es explorar y visualizar los datos para obtener información relevante sobre el uso de bicicletas en diferentes condiciones.

## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos:

- **carga_datos.py**: Contiene la función para cargar y preparar el conjunto de datos.
- **analisis.py**: Incluye funciones para explorar y analizar los datos.
- **graficos.py**: Proporciona funciones para la visualización gráfica de los datos.
- **main.py**: Script principal que orquesta la ejecución de los módulos anteriores.

## Requisitos

**Crear y activar el entorno virtual:**

   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

Puedes instalar las dependencias utilizando `pip`:

```bash
pip install pandas matplotlib seaborn scikit-learn ucimlrepo
```
Alternativamente, se pueden instalar todas las dependencias con:

```bash
pip install -r requirements.txt
```