import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('50000_minus_3000_patientconcerns.csv')

print(df.size)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['question'])

cosine_sim_matrix = cosine_similarity(X)

duplicates = []
for i in range(len(cosine_sim_matrix)):
    for j in range(i+1, len(cosine_sim_matrix)):
        if cosine_sim_matrix[i][j] > 0.9:
            duplicates.append((i,j))

df.drop_duplicates(subset=['text'], inplace=True)
for i, j in duplicates:
    df.drop(j, inplace=True)

print(df.size)

df.to_csv('unique50000.csv', index=False)