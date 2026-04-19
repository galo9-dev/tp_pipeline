📄 Análisis de texto - CorpusLenguajes (NLP)
📌 Descripción

En este proyecto se realizó un análisis de texto utilizando Python aplicando técnicas básicas de Procesamiento de Lenguaje Natural (NLP).

El objetivo fue procesar un corpus de texto (CorpusLenguajes.txt) para limpiar los datos, normalizarlos y extraer información relevante como frecuencias de palabras y representación vectorial mediante TF-IDF.

🛠️ Tecnologías utilizadas
Python 3
NLTK
Matplotlib
scikit-learn

Además, se utilizaron módulos estándar de Python:

collections (Counter)
os (gestión de archivos)
📚 Funcionalidades implementadas

El programa realiza las siguientes tareas:

🔹 Preprocesamiento del texto
Tokenización del texto
Conversión a minúsculas
Eliminación de caracteres no alfabéticos
Eliminación de stopwords (español e inglés)
Lematización de palabras
🔹 Análisis del corpus
Generación del corpus procesado
Conteo de frecuencia de palabras
Identificación de las palabras más frecuentes
Identificación de la palabra menos utilizada
Detección de palabras repetidas dentro de cada oración
🔹 Representación vectorial
Cálculo de la matriz TF-IDF usando TfidfVectorizer
🔹 Visualización
Gráfico de barras con las palabras más frecuentes utilizando Matplotlib