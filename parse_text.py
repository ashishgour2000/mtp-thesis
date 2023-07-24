import csv
import pandas as pd

#filename = 'healthcaremagic_dialogue_4.txt'
filename = 'icliniq_dialogue.txt'

list1 = []
count=0
link=0
description=0
dialogue=0
patient=0
doctor=0
patient_value =""
doctor_value=""
empty_line_count = 0
list_not_in_csv = []
with open(filename, encoding="utf8") as f:
    #contents = f.readlines()
    for line in f.readlines():
        if line=="":
            empty_line_count = empty_line_count +1
        elif line[:2] == "id":
            if count != 0:
                dialogue=0
                doctor=0
                list2.append(doctor_value)
                doctor_value = ""
                if len(list2) == 5:
                    #print(list2)
                    list1.append(list2)
                else:
                    list_not_in_csv.append(list2)
            list2 = []
            list2.append(count)
            count = count+1
            link=1
        elif link == 1:
            link_value = line
            list2.append(link_value)
            link=0
        elif line[:11] == "Description":
            description=1
        elif description == 1:
            description_value = line
            list2.append(description_value)
            description=0
        elif line[:8] == "Dialogue":
            dialogue=1
        elif dialogue == 1:
            if line[:8] == "Patient:":
                patient=1
            elif line[:7] == "Doctor:":
                doctor=1
                patient=0
                list2.append(patient_value)
                patient_value = ""
            elif patient==1:
                patient_value = patient_value + line
            elif doctor==1:
                doctor_value = doctor_value + line
            #elif line=="":
            #    empty_line_count = empty_line_count +1
            #    dialogue=0
            #    doctor=0
            #    list2.append(doctor_value)
            #    doctor_value = ""

list2.append(doctor_value)
#list1.append(list2)
if len(list2) == 5:
    #print(list2)
    list1.append(list2)
else:
    list_not_in_csv.append(list2)

f.close()

frame = pd.DataFrame(list1, columns = ['id', 'link', 'description', 'patient_dialogue', 'doctor_dialogue'])
frame.to_csv('icliniq_dialogue.csv')