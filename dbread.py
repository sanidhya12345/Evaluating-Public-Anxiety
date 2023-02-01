import math
import pandas as pd

df=pd.read_csv('twitter_English.csv',usecols=['tweet','Name','Email'])
listtweet=[]
listname=[]
listemail=[]
for i in df['Email']:
    listemail.append(i)
for i in df['tweet']:
    listtweet.append(i)
for i in df['Name']:
    listname.append(i)
dict={listtweet[i]:listname[i] for i in range(0,500)}
dict2={listtweet[i]:listemail[i] for i in range(0,500)}
keyword=input('Enter Keyword:- ')
# for i in listtweet:
#     if i.find(keyword)!=-1:
#             if dict.get(i)!=None:
#                 print(dict.get(i)+" "+dict2.get(i))

for i in listtweet:
    count=0
    if i.find(keyword)!=-1:
        count+=1
        if dict.get(i)!=None:
            print(dict.get(i)+'  ',dict2.get(i)+'  ',(count/len(i))*100)
