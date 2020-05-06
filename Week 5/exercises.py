import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def divorce_percentage():
    filename = "Week 5\divorced_data.csv"
    df = pd.read_csv(filename, delimiter=';')
    
    divorced = df.loc[df['CIVILSTAND'] == 'Fraskilt'].iloc[:, 2]
    total = df.loc[df['CIVILSTAND'] == 'I alt'].iloc[:, 2] 
    time = df.loc[df['CIVILSTAND'] == 'Fraskilt'].iloc[:,1]

    percentage = [(divorced.to_numpy()[i] / total.to_numpy()[i]) * 100 for i in range(len(total))]

    plt.plot(time, percentage)
    plt.xticks(rotation=90)
    plt.show()


# divorce_percentage()


def never_married_highest():

    filename = "Week 5\\never_married_data.csv"
    df = pd.read_csv(filename, delimiter=';')

    total = df.loc[df['CIVILSTAND'] == 'I alt'].iloc[:,3]
    never_married = df.loc[df['CIVILSTAND'] == 'Ugift'].iloc[:,3]
    område = df.loc[df['CIVILSTAND'] == 'I alt'].iloc[:,1]

    percentage = [(never_married.to_numpy()[i] / total.to_numpy()[i]) * 100 for i in range(len(total))]

    plt.bar(område, percentage)
    plt.show()

    
# never_married_highest()

def marital_status():

    filename = "Week 5\marital_status.csv"
    df = pd.read_csv(filename, delimiter=';')

    df.plot.bar(x='CIVILSTAND')
    plt.show()
    

# marital_status()


def married_vs_never_married():

    filename = "Week 5\married_never_married.csv"
    df = pd.read_csv(filename, delimiter=';')

    df1 = df.loc[df['CIVILSTAND'] == 'Gift/separeret']
    df2 = df.loc[df['CIVILSTAND'] == 'Ugift']

    plt.bar(df1['ALDER'], df1['INDHOLD'])
    plt.bar(df2['ALDER'], df2['INDHOLD'])
    plt.show()

# married_vs_never_married()
