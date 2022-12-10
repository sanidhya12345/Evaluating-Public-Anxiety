import pandas as pd
import csv
from google.colab import files
uploaded = files.upload()
titanic_data = pd.read_csv('twitter_English.csv')
tweet=titanic_data['tweet']
print(titanic_data)
list=['anxiety','hello','baby','bye','depression']
listcount=[]
count=0;
for j in list:
  countTemp=0;
  for i in tweet:
      if i.find(j) != -1:
          countTemp+=1;
          count+=1;
  listcount.append(countTemp)
dict={list[i]:listcount[i] for i in range(0,len(list))}
print(dict)
lst=[]
for i in range(0,len(list)):
   lst.append(list[i])
   lst.append(listcount[i])
   lst.append(listcount[i]/count)
print(lst)

key_list = ["topic", "count","score"]
n=len(lst)
res = []
for idx in range(0, n, 3):
  res.append({key_list[0]: lst[idx],  key_list[1] : lst[idx + 1], key_list[2]:lst[idx+2]})
print(res)

col_name=["topic","count","score"]
with open("export.csv", 'w') as csvFile:
        wr = csv.DictWriter(csvFile, fieldnames=col_name)
        wr.writeheader()
        for ele in res:
            wr.writerow(ele)
 es = pd.read_csv('export.csv')
print(es)
es.sort_values(["score"], 
                    axis = 0,
                    ascending = [False], 
                    inplace = True)
print(es)
import matplotlib.pyplot as plt
topic = es["topic"]
count = es["count"]
plt.pie(count, labels = topic,autopct = '%1.1f%%’,  startangle = 140, shadow = True)
plt.title("ANXIETY")
plt.show()
