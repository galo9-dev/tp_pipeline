import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter


with open("c:/Users/galog/Documents/tp_scudero/CorpusLenguajes.txt", "r", encoding="utf-8") as f:
    corpus = f.readlines()


stop_words = set(stopwords.words('spanish') + stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

corpus_procesado = []

for doc in corpus:
    tokens = nltk.word_tokenize(doc.lower())
    
    
    tokens = [t for t in tokens if t.isalpha()]
    
    
    tokens = [t for t in tokens if t not in stop_words]
    
    
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    
    corpus_procesado.append(" ".join(tokens))

print("\n--- Corpus procesado ---")
for doc in corpus_procesado:
    print(doc)


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus_procesado)

print("\n--- Matriz TF-IDF ---")
print(X.toarray())

print("\n--- Vocabulario ---")
print(vectorizer.get_feature_names_out())


todas_palabras = " ".join(corpus_procesado).split()
conteo = Counter(todas_palabras)


top_6 = conteo.most_common(6)
print("\nTop 6 palabras:", top_6)


menos_usada = conteo.most_common()[-1]
print("Palabra menos usada:", menos_usada)


print("\n--- Repeticiones por oración ---")
for doc in corpus_procesado:
    palabras = doc.split()
    c = Counter(palabras)
    repetidas = [p for p, v in c.items() if v > 1]
    if repetidas:
        print(doc, "->", repetidas)


palabras = [p[0] for p in top_6]
frecuencias = [p[1] for p in top_6]

plt.bar(palabras, frecuencias)
plt.title("Distribución de Frecuencia (Top 6)")
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")
plt.show()