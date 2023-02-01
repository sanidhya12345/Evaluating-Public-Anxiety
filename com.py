import csv
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('twitter_English.csv',usecols=['tweet','Name','Email'])
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list=['anxiety','Suicide','lockdown','please','chronic','fatigue','love','Sad','pain']
for i in range(0,100):
    list1.append(df['tweet'][i])
for i in range(100,200):
    list2.append(df['tweet'][i])
for i in range(200,300):
    list3.append(df['tweet'][i])
for i in range(300,400):
    list4.append(df['tweet'][i])
for i in range(400,500):
    list5.append(df['tweet'][i])
key_list=["topic","count","score"]
#community 1:-
countcom1=0
lst1=[]
lstcount1=[]
for j in list:
    countTemp=0
    for k in list1:
        if k.find(j)!=-1:
            countTemp+=1
            countcom1+=1
    lstcount1.append(countTemp)
dct1={list[i]:lstcount1[i] for i in range(0,len(list))}
for i in range(0,len(list)):
    lst1.append(list[i])
    lst1.append(lstcount1[i])
    lst1.append(lstcount1[i]/countcom1)

n=len(lst1)
res1=[]
for idx in range(0,n,3):
    res1.append({key_list[0]:lst1[idx],key_list[1]:lst1[idx+1],key_list[2]:lst1[idx+2]})

with open("export1.csv",'w') as csvFile:
    wr=csv.DictWriter(csvFile,fieldnames=key_list)
    wr.writeheader()
    for ele in res1:
        wr.writerow(ele)

es1=pd.read_csv('export1.csv')
topic1=es1["topic"]
count1=es1["count"]
plt.pie(count1,labels=topic1,autopct='%1.1f%%',startangle=140,shadow=True)
plt.title("Community 1 Anxiety")
plt.show()

