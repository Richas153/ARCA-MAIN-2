# **Proyecto ARCA: Analizador de Riesgo de Candidatos Automatizado**

## **1. Descripción General**

ARCA es un sistema automatizado que analiza transcripciones de entrevistas de trabajo para evaluar el riesgo de deserción (attrition) y la idoneidad de los candidatos para un puesto. El sistema utiliza un modelo de lenguaje avanzado (Gemini) para procesar las transcripciones, aplicar un conjunto de reglas de negocio estrictas y generar un análisis estructurado.

El objetivo principal es estandarizar y acelerar el proceso de evaluación de candidatos, proporcionando a los reclutadores datos consistentes y auditables para la toma de decisiones.

## **2. Características Principales**

*   **Análisis Automatizado:** Procesa archivos de transcripción (`.vtt`) de forma automática.
*   **Base de Datos Centralizada:** Almacena todos los resultados de forma segura en una base de datos SQLite para persistencia y consultas.
*   **Validación de Datos:** Incorpora un sistema de validación para asegurar la calidad e integridad de cada análisis antes de ser guardado.
*   **Exportación Consolidada:** Genera un único archivo `consolidated_results.csv` con los resultados de todos los candidatos analizados.
*   **Motor de Reglas Detallado:** Opera sobre un manual de criterios exhaustivo definido en `GEMINI.md` y `gemini_evaluation_prompt.txt`.

## **3. Tecnologías Utilizadas**

*   **Lenguaje de Programación:** Python 3
*   **Base de Datos:** SQLite 3
*   **Modelo de Lenguaje:** Google Gemini

## **4. Estructura del Proyecto**

```
/
├── 📂 in/
│   └── 📄 *.vtt (Aquí se colocan las transcripciones a analizar)
├── 📂 out/
│   └── 📄 consolidated_results.csv (Aquí se genera el resultado final)
├── 📄 main.py (Script principal que orquesta todo el proceso)
├── 📄 database_setup.py (Crea la base de datos y la tabla si no existen)
├── 📄 arca_db.sqlite (La base de datos donde se guardan los resultados)
├── 📄 GEMINI.md (El manual de criterios completo)
├── 📄 gemini_evaluation_prompt.txt (El prompt de instrucciones para el modelo)
└── 📄 requirements.txt (Las dependencias de Python necesarias)
```

## **5. Instalación**

Para configurar el entorno, instala las dependencias de Python necesarias ejecutando:

```bash
pip install -r requirements.txt
```

## **6. Modo de Uso**

El sistema está diseñado para ser simple y reutilizable:

1.  **Añadir Transcripciones:** Coloca todos los nuevos archivos de entrevista en formato `.vtt` dentro de la carpeta `in/`.
2.  **Ejecutar el Análisis:** Abre una terminal en la raíz del proyecto y ejecuta el script principal:

    ```bash
    python main.py
    ```

El script se encargará del resto: detectará los archivos nuevos, los procesará uno por uno, guardará los resultados validados en la base de datos y finalmente actualizará el archivo `out/consolidated_results.csv` con todos los datos.

## **7. Flujo de Trabajo Interno**

El proceso automatizado sigue estos pasos:
1.  **Verificación de la Base de Datos:** Se asegura de que `arca_db.sqlite` y su tabla existan.
2.  **Detección de Archivos Nuevos:** Compara los archivos en la carpeta `in/` con los registros en la base de datos para procesar únicamente las entrevistas pendientes.
3.  **Análisis y Validación por Archivo:**
    *   Un modelo de IA analiza una transcripción.
    *   El resultado pasa por un filtro de validación en `main.py` que confirma el formato correcto.
4.  **Almacenamiento:** Los resultados validados se guardan en la base de datos SQLite.
5.  **Exportación:** Al finalizar, todos los datos de la base de datos se exportan al archivo `consolidated_results.csv`.
