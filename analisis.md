📊 Análisis de resultados

Durante el desarrollo del análisis me surgió una duda inicial respecto al idioma del procesamiento. Si bien el corpus se encuentra mayormente en inglés, también incluye el término en español “lematizar”, lo que llevó a considerar si debía incluirse en el análisis o ser filtrado. Finalmente, decidi mantener todos los términos presentes en el corpus, independientemente del idioma, para no perder información relevante.

🔝 Frecuencia de palabras

Las palabras más frecuentes obtenidas fueron:

lematizar (10 apariciones)
python (7)
javascript (7)
cplus (5)
rust (5)
interpreted (3)

Se observa que predominan términos relacionados con lenguajes de programación y conceptos técnicos. En particular, la alta frecuencia de “lematizar” puede deberse a su repetición en la introducción del corpus, lo que influye en los resultados.

Por otro lado, la palabra menos utilizada fue:

programmer (1 aparición)
📚 Vocabulario

El vocabulario obtenido incluye una variedad de términos técnicos vinculados al desarrollo de software, tales como:

python, javascript, java, rust
compiled, interpreted, statically, dynamically
backend, server, cloud
artificial, intelligence, data, science

Esto indica que el corpus está enfocado en conceptos de programación y tecnología, con una mezcla de términos teóricos y prácticos.

🔢 Matriz TF-IDF

La matriz TF-IDF permite representar cada documento del corpus como un vector numérico, donde cada valor indica la importancia de una palabra dentro de ese documento en relación con el resto del corpus.

En los resultados obtenidos se puede observar que:

La mayoría de los valores son cercanos a 0, lo que indica baja relevancia de muchas palabras en ciertos documentos.
Algunas palabras presentan valores más altos, lo que refleja su mayor importancia dentro de documentos específicos.
Esta representación es útil para tareas posteriores como clasificación de textos o análisis de similitud entre documentos.
🧠 Interpretación general

El análisis muestra cómo, a través del preprocesamiento (tokenización, eliminación de stopwords y lematización), es posible reducir el ruido del texto y destacar los términos más relevantes.

Sin embargo, también se evidencia que la presencia de palabras repetidas en ciertas secciones del corpus (como “lematizar”) puede sesgar los resultados, lo cual es importante tener en cuenta al interpretar las frecuencias.

📌 Conclusión

En conclusión, el procesamiento del corpus permitió identificar las palabras más relevantes y comprender la estructura temática del texto.

El uso de técnicas como TF-IDF resultó fundamental para transformar el texto en una representación numérica, facilitando futuros análisis más avanzados dentro del campo del Procesamiento de Lenguaje Natural.