import math
from numpy.random import rand
import pandas as pd
import numpy as np
import random
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
input_vector=[]
for i in listtweet:
    count=0
    if i.find(keyword)!=-1:
        count+=1
        if dict.get(i)!=None:
            input_vector.append((count/len(i))*100)
inp=np.array(input_vector)
print(input_vector)

lowerrange=-1/math.sqrt(len(input_vector))
higherrange=1/math.sqrt(len(input_vector))
# print(weight1)
# # print(weight2)
# dotproduct1=np.dot(input_vector,weight1)
# dotproduct2=np.dot(input_vector,weight2)
# print(dotproduct1)
# print(dotproduct2)
numbers = rand(1000)
# scale to the desired range
scaled = lowerrange + numbers * (higherrange - lowerrange)
# print(lowerrange)
# print(higherrange)
# print(scaled.mean())
# print(scaled.std())
weight=[]
for i in range(len(input_vector)):
    weight.append(scaled.mean())
dotproduct=np.dot(input_vector,weight)
print(dotproduct)
bias = np.array([0.0])
def sigmoid(x):
   return 1 / (1 + np.exp(-x))

def make_prediction(input_vector, weights, bias):
   layer_1 = np.dot(input_vector, weights) + bias
   layer_2 = sigmoid(layer_1)
   return layer_2
prediction = make_prediction(input_vector, weight, bias)
print(prediction[0])