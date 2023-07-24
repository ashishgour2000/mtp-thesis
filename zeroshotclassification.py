!pip install transformers

import pandas as pd
from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=0)

headlines = pd.read_csv('/content/drive/MyDrive/mtp/vomit.csv')

strings = headlines.question.values
sequence = list(strings)

candidate_labels = ["eating", "headache", "discomfort", "pregnancy", "children", "drugs"]
output = classifier(sequence, candidate_labels)
output

op = pd.DataFrame(output)
op

doc_candidate_labels = ["Sexology", "Obstetrics and Gynaecology", "Neurology", "Paediatrics", "Internal Medicine", "Physician", "Diabetology", "ENT", "Ayurveda", "Orthopaedics", "Dietetics/Nutrition", "Psychiatry", "Pulmonology", "Surgical Gastroenterology"]
doc_output = classifier(sequence, doc_candidate_labels, multi_class=True)
doc_output