import pandas as pd
import csv

data = pd.read_csv("1_coldandcough_result.csv")

myDict = {}
myDict["nose"] = []
myDict["throat"] = []
myDict["earpain"] = []
myDict["medication"] = []
myDict["children"] = []

for x,y in zip(data.labels, data.sequence):
  s = x
  s = s.replace('[','')
  s = s.replace(']','')
  s = s.replace("'","")
  s = s.replace(" ","")
  my_list = s.split(",")
  myDict[my_list[0]].append(y)


for x in myDict:
  frame = pd.DataFrame(myDict[x], columns = ['question'])
  ss = "1_" + str(x) + ".csv"
  frame.to_csv(ss)