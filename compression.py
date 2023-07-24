import csv
import pandas as pd

data_list = []
filename = 'patient_unique.csv'
i = 0
with open(filename, 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	next(csv_reader) #jump to 2nd line OR ignore first line
	for line in csv_reader:
		print(i)
		#if (i%550)==0:
		if i<1000:
			element_list = []
			for col in line:
				element_list.append(col)
			data_list.append(element_list)
		i=i+1

try:
	frame = pd.DataFrame(data_list, columns = ['question', 'answer', 'drug', 'doctor', 'speciality'])
except:
	frame = pd.DataFrame(data_list, columns = ['serial no.', 'question', 'answer', 'drug', 'doctor', 'speciality'])

frame.to_csv('1000.csv')