import pandas as pd
from tkinter import *
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math
from numpy.random import rand
import numpy as np
root=Tk()
root.geometry('800x600')
root.title("ADS")
l1=Label(root,text="Anxiety Detection System",font=('times new roman',20),fg="blue").pack()
Label(root,text=" ").pack()
l2=Label(root,text="CHOOSE MODE",font=('times new roman', 18),fg="green").pack()
Label(root,text=" ").pack()

def tropical():
    f=Toplevel()
    f.geometry('800x600')
    def showData():
        d=Toplevel()
        d.geometry('800x600')
        text = Text(d, width=100, height=100)
        df = pd.read_csv('twitter_English.csv', usecols=['tweet', 'Name','Email'])
        listtweet = []
        listname = []
        listemail = []
        for i in df['Email']:
            listemail.append(i)
        for i in df['tweet']:
            listtweet.append(i)
        for i in df['Name']:
            listname.append(i)
        dict = {listtweet[i]: listname[i] for i in range(0, 500)}
        dict2 = {listtweet[i]: listemail[i] for i in range(0, 500)}
        for i in listtweet:
            count=0
            if i.find(keyword.get()) != -1:
                count+=1
                if dict.get(i) != None:
                    text.insert(END, dict.get(i)+"   "+dict2.get(i)+"    "+str((count/len(i))*100)+"    " +'\n')
        text.pack()
    keyword=StringVar()
    Top = Frame(f, bd=2, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(f, height=200)
    Form.pack(side=TOP, pady=20)
    lbl_title = Label(Top, text="Anti-Suicidal-System", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_keyword= Label(Form, text="KeyWord", font=('arial', 14), fg="blue", bd=15)
    lbl_keyword.grid(row=0, sticky="e")
    kword = Entry(Form, textvariable=keyword, font=(14))
    kword.grid(row=0, column=1)
    Button(f, text='Show Data', command=showData).pack()
    Button(f,text='Back',command=root.destroy).pack()
def statistical():
    t=Toplevel()
    t.geometry('800x600')
    list = ['anxiety', 'Suicide', 'lockdown','fatigue', 'love', 'Sad', 'pain']
    df = pd.read_csv('twitter_English.csv', usecols=['tweet', 'Name', 'Email'])
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    # community 1:-
    def com1():
        cm1=Toplevel()
        cm1.geometry('800x600')
        for i in range(0, 100):
            list1.append(df['tweet'][i])
        key_list = ["topic", "count", "score"]
        countcom1 = 0
        lst1 = []
        lstcount1 = []
        for j in list:
            countTemp = 0
            for k in list1:
                if k.find(j) != -1:
                    countTemp += 1
                    countcom1 += 1
            lstcount1.append(countTemp)
        dct1 = {list[i]: lstcount1[i] for i in range(0, len(list))}
        for i in range(0, len(list)):
            lst1.append(list[i])
            lst1.append(lstcount1[i])
            lst1.append(lstcount1[i] / countcom1)

        n = len(lst1)
        res1 = []
        for idx in range(0, n, 3):
            res1.append({key_list[0]: lst1[idx], key_list[1]: lst1[idx + 1], key_list[2]: lst1[idx + 2]})

        with open("export1.csv", 'w') as csvFile:
            wr = csv.DictWriter(csvFile, fieldnames=key_list)
            wr.writeheader()
            for ele in res1:
                wr.writerow(ele)

        es1 = pd.read_csv('export1.csv')
        topic1 = es1["topic"]
        count1 = es1["count"]
        # plt.pie(count1, labels=topic1, autopct='%1.1f%%', startangle=140, shadow=True)
        # plt.title("Community 1 Anxiety")
        # plt.show()
        fig = Figure()  # create a figure object
        ax = fig.add_subplot(111)  # add an Axes to the figure
        ax.pie(count1, radius=1, labels=topic1, autopct='%1.1f%%', shadow=True, )
        chart1 = FigureCanvasTkAgg(fig, cm1)
        chart1.get_tk_widget().pack()
        input_vector1=[lstcount1[i]/countcom1 for i in range(0,len(lstcount1))]
        lowerrange = -1 / math.sqrt(len(input_vector1))
        higherrange = 1 / math.sqrt(len(input_vector1))
        numbers = rand(1000)
        # scale to the desired range
        scaled = lowerrange + numbers * (higherrange - lowerrange)
        weight1 = []
        for i in range(len(input_vector1)):
            weight1.append(scaled.mean())
        dotproduct = np.dot(input_vector1, weight1)
        bias = np.array([0.0])
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))
        def make_prediction(input_vector, weights, bias):
            layer_1 = np.dot(input_vector, weights) + bias
            layer_2 = sigmoid(layer_1)
            return layer_2
        prediction = make_prediction(input_vector1, weight1, bias)
        text = Text(cm1, width=100, height=5)
        text.insert(END,"Overall Anxiety Score:- "+str(prediction[0]))
        text.pack()
        Button(cm1, text='Back', command=cm1.destroy).pack()
    def com2():
        cm2 = Toplevel()
        cm2.geometry('800x600')
        for i in range(100, 200):
            list2.append(df['tweet'][i])
        key_list = ["topic", "count", "score"]
        countcom2 = 0
        lst2 = []
        lstcount2 = []
        for j in list:
            countTemp = 0
            for k in list2:
                if k.find(j) != -1:
                    countTemp += 1
                    countcom2 += 1
            lstcount2.append(countTemp)
        dct1 = {list[i]: lstcount2[i] for i in range(0, len(list))}
        for i in range(0, len(list)):
            lst2.append(list[i])
            lst2.append(lstcount2[i])
            lst2.append(lstcount2[i] / countcom2)

        n = len(lst2)
        res2 = []
        for idx in range(0, n, 3):
            res2.append({key_list[0]: lst2[idx], key_list[1]: lst2[idx + 1], key_list[2]: lst2[idx + 2]})

        with open("export2.csv", 'w') as csvFile:
            wr = csv.DictWriter(csvFile, fieldnames=key_list)
            wr.writeheader()
            for ele in res2:
                wr.writerow(ele)

        es2 = pd.read_csv('export2.csv')
        topic2 = es2["topic"]
        count2 = es2["count"]
        # plt.pie(count1, labels=topic1, autopct='%1.1f%%', startangle=140, shadow=True)
        # plt.title("Community 1 Anxiety")
        # plt.show()
        fig = Figure()  # create a figure object
        ax = fig.add_subplot(111)  # add an Axes to the figure
        ax.pie(count2, radius=1, labels=topic2, startangle=140,autopct='%1.1f%%', shadow=True, )
        chart1 = FigureCanvasTkAgg(fig, cm2)
        chart1.get_tk_widget().pack()
        input_vector1 = [lstcount2[i] / countcom2 for i in range(0, len(lstcount2))]
        lowerrange = -1 / math.sqrt(len(input_vector1))
        higherrange = 1 / math.sqrt(len(input_vector1))
        numbers = rand(1000)
        # scale to the desired range
        scaled = lowerrange + numbers * (higherrange - lowerrange)
        weight1 = []
        for i in range(len(input_vector1)):
            weight1.append(scaled.mean())
        bias = np.array([0.0])
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))
        def make_prediction(input_vector, weights, bias):
            layer_1 = np.dot(input_vector, weights) + bias
            layer_2 = sigmoid(layer_1)
            return layer_2

        prediction = make_prediction(input_vector1, weight1, bias)
        text = Text(cm2, width=100, height=5)
        text.insert(END, "Overall Anxiety Score:- " + str(prediction[0]))
        text.pack()
        Button(cm2, text='Back', command=cm2.destroy).pack()
    def com3():
        cm3 = Toplevel()
        cm3.geometry('800x600')
        for i in range(200, 300):
            list3.append(df['tweet'][i])
        key_list = ["topic", "count", "score"]
        countcom2 = 0
        lst2 = []
        lstcount2 = []
        for j in list:
            countTemp = 0
            for k in list3:
                if k.find(j) != -1:
                    countTemp += 1
                    countcom2 += 1
            lstcount2.append(countTemp)
        dct1 = {list[i]: lstcount2[i] for i in range(0, len(list))}
        for i in range(0, len(list)):
            lst2.append(list[i])
            lst2.append(lstcount2[i])
            lst2.append(lstcount2[i] / countcom2)

        n = len(lst2)
        res2 = []
        for idx in range(0, n, 3):
            res2.append({key_list[0]: lst2[idx], key_list[1]: lst2[idx + 1], key_list[2]: lst2[idx + 2]})

        with open("export3.csv", 'w') as csvFile:
            wr = csv.DictWriter(csvFile, fieldnames=key_list)
            wr.writeheader()
            for ele in res2:
                wr.writerow(ele)
        es2 = pd.read_csv('export3.csv')
        topic2 = es2["topic"]
        count2 = es2["count"]
        # plt.pie(count1, labels=topic1, autopct='%1.1f%%', startangle=140, shadow=True)
        # plt.title("Community 1 Anxiety")
        # plt.show()
        fig = Figure()  # create a figure object
        ax = fig.add_subplot(111)  # add an Axes to the figure
        ax.pie(count2, radius=1, labels=topic2, startangle=140,autopct='%1.1f%%', shadow=True, )
        chart1 = FigureCanvasTkAgg(fig, cm3)
        chart1.get_tk_widget().pack()
        input_vector1 = [lstcount2[i] / countcom2 for i in range(0, len(lstcount2))]
        lowerrange = -1 / math.sqrt(len(input_vector1))
        higherrange = 1 / math.sqrt(len(input_vector1))
        numbers = rand(1000)
        # scale to the desired range
        scaled = lowerrange + numbers * (higherrange - lowerrange)
        weight1 = []
        for i in range(len(input_vector1)):
            weight1.append(scaled.mean())
        bias = np.array([0.0])
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))
        def make_prediction(input_vector, weights, bias):
            layer_1 = np.dot(input_vector, weights) + bias
            layer_2 = sigmoid(layer_1)
            return layer_2
        prediction = make_prediction(input_vector1, weight1, bias)
        text = Text(cm3, width=100, height=5)
        text.insert(END, "Overall Anxiety Score:- " + str(prediction[0]))
        text.pack()
        Button(cm3, text='Back', command=cm3.destroy).pack()
    def com4():
        cm4 = Toplevel()
        cm4.geometry('800x600')
        for i in range(300, 400):
            list4.append(df['tweet'][i])
        key_list = ["topic", "count", "score"]
        countcom2 = 0
        lst2 = []
        lstcount2 = []
        for j in list:
            countTemp = 0
            for k in list4:
                if k.find(j) != -1:
                    countTemp += 1
                    countcom2 += 1
            lstcount2.append(countTemp)
        dct1 = {list[i]: lstcount2[i] for i in range(0, len(list))}
        for i in range(0, len(list)):
            lst2.append(list[i])
            lst2.append(lstcount2[i])
            lst2.append(lstcount2[i] / countcom2)

        n = len(lst2)
        res2 = []
        for idx in range(0, n, 3):
            res2.append({key_list[0]: lst2[idx], key_list[1]: lst2[idx + 1], key_list[2]: lst2[idx + 2]})

        with open("export4.csv", 'w') as csvFile:
            wr = csv.DictWriter(csvFile, fieldnames=key_list)
            wr.writeheader()
            for ele in res2:
                wr.writerow(ele)
        es2 = pd.read_csv('export4.csv')
        topic2 = es2["topic"]
        count2 = es2["count"]
        # plt.pie(count1, labels=topic1, autopct='%1.1f%%', startangle=140, shadow=True)
        # plt.title("Community 1 Anxiety")
        # plt.show()
        fig = Figure()  # create a figure object
        ax = fig.add_subplot(111)  # add an Axes to the figure
        ax.pie(count2, radius=1, labels=topic2, startangle=140,autopct='%1.1f%%', shadow=True, )
        chart1 = FigureCanvasTkAgg(fig, cm4)
        chart1.get_tk_widget().pack()
        input_vector1 = [lstcount2[i] / countcom2 for i in range(0, len(lstcount2))]
        lowerrange = -1 / math.sqrt(len(input_vector1))
        higherrange = 1 / math.sqrt(len(input_vector1))
        numbers = rand(1000)
        # scale to the desired range
        scaled = lowerrange + numbers * (higherrange - lowerrange)
        weight1 = []
        for i in range(len(input_vector1)):
            weight1.append(scaled.mean())
        bias = np.array([0.0])
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))
        def make_prediction(input_vector, weights, bias):
            layer_1 = np.dot(input_vector, weights) + bias
            layer_2 = sigmoid(layer_1)
            return layer_2
        prediction = make_prediction(input_vector1, weight1, bias)
        text = Text(cm4, width=100, height=5)
        text.insert(END, "Overall Anxiety Score:- " + str(prediction[0]))
        text.pack()
        Button(cm4, text='Back', command=cm4.destroy).pack()
    def com5():
        cm5 = Toplevel()
        cm5.geometry('800x600')
        for i in range(400, 500):
            list5.append(df['tweet'][i])
        key_list = ["topic", "count", "score"]
        countcom2 = 0
        lst2 = []
        lstcount2 = []
        for j in list:
            countTemp = 0
            for k in list5:
                if k.find(j) != -1:
                    countTemp += 1
                    countcom2 += 1
            lstcount2.append(countTemp)
        dct1 = {list[i]: lstcount2[i] for i in range(0, len(list))}
        for i in range(0, len(list)):
            lst2.append(list[i])
            lst2.append(lstcount2[i])
            lst2.append(lstcount2[i] / countcom2)

        n = len(lst2)
        res2 = []
        for idx in range(0, n, 3):
            res2.append({key_list[0]: lst2[idx], key_list[1]: lst2[idx + 1], key_list[2]: lst2[idx + 2]})

        with open("export5.csv", 'w') as csvFile:
            wr = csv.DictWriter(csvFile, fieldnames=key_list)
            wr.writeheader()
            for ele in res2:
                wr.writerow(ele)
        es2 = pd.read_csv('export5.csv')
        topic2 = es2["topic"]
        count2 = es2["count"]
        # plt.pie(count1, labels=topic1, autopct='%1.1f%%', startangle=140, shadow=True)
        # plt.title("Community 1 Anxiety")
        # plt.show()
        fig = Figure()  # create a figure object
        ax = fig.add_subplot(111)  # add an Axes to the figure
        ax.pie(count2, radius=1, labels=topic2, startangle=140,autopct='%1.1f%%', shadow=True, )
        chart1 = FigureCanvasTkAgg(fig, cm5)
        chart1.get_tk_widget().pack()
        input_vector1 = [lstcount2[i] / countcom2 for i in range(0, len(lstcount2))]
        lowerrange = -1 / math.sqrt(len(input_vector1))
        higherrange = 1 / math.sqrt(len(input_vector1))
        numbers = rand(1000)
        # scale to the desired range
        scaled = lowerrange + numbers * (higherrange - lowerrange)
        weight1 = []
        for i in range(len(input_vector1)):
            weight1.append(scaled.mean())
        bias = np.array([0.0])
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))
        def make_prediction(input_vector, weights, bias):
            layer_1 = np.dot(input_vector, weights) + bias
            layer_2 = sigmoid(layer_1)
            return layer_2
        prediction = make_prediction(input_vector1, weight1, bias)
        text = Text(cm5, width=100, height=5)
        text.insert(END, "Overall Anxiety Score:- " + str(prediction[0]))
        text.pack()
        Button(cm5, text='Back', command=cm5.destroy).pack()

    Label(t, text=" ").pack()
    Label(t, text=" ").pack()
    Button(t,text='Community 1',height=1,width=20,fg="red",bg="yellow",command=com1).pack()
    Label(t, text=" ").pack()
    Label(t, text=" ").pack()
    Button(t,text='Community 2',height=1,width=20,fg="red",bg="pink",command=com2).pack()
    Label(t, text=" ").pack()
    Label(t, text=" ").pack()
    Button(t, text='Community 3', height=1, width=20, fg="orange", bg="white", command=com3).pack()
    Label(t, text=" ").pack()
    Label(t, text=" ").pack()
    Button(t, text='Community 4', height=1, width=20, fg="orange", bg="white", command=com4).pack()
    Label(t, text=" ").pack()
    Label(t, text=" ").pack()
    Button(t, text='Community 5', height=1, width=20, fg="orange", bg="white", command=com5).pack()
    Label(t, text=" ").pack()
    Label(t, text=" ").pack()
    Button(t, text='Back', command=t.destroy).pack()
b1 = Button(root, text="Structural Anxiety", font=('times new roman',12),height=1,width=20,fg="red",bg="yellow",command=statistical).pack()
Label(root, text=" ").pack()
b2 = Button(root, text="Topical Anxiety", font=('times new roman',12), height=1, width=20, bg="yellow",command=tropical).pack()
root.mainloop()