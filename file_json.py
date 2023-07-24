import json
import csv
import pandas as pd

f = open('english-test.json')

data = json.load(f)
  
list1 = []
for i in data:
    list2 = []
    list2.append(i["description"])
    list2.append(i["utterances"][0][9:])
    list2.append(i["utterances"][1][8:])
    list1.append(list2)

frame = pd.DataFrame(list1, columns = ['description', 'question', 'answer'])
frame.to_csv('medical_dialogue_test.csv')

f.close()