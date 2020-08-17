import pandas as pd
from matplotlib import pyplot

pyplot.style.use('fivethirtyeight')

data = pd.read_csv('data3.csv')
ids = data['Responder_id']
ages = data['Age']

#pyplot.hist(ages, bins= 5)
#if you just imput a random number for the bins - it will divide the total data by that number to determine the divisions

bin = [10,20,30,40,50,60,70,80,90,100]
#when you define a bin, you can decide where you want the values to start from ex. if you only want data from people over 30 - you can make it the first value of the bins

pyplot.hist(ages, bins=bin, edgecolor= 'black',log=True)

median_age = 29
color = '#fc4f30'

pyplot.axvline(median_age, color='black', label='Age Median')

pyplot.legend()

pyplot.title('Ages of Respondents')
pyplot.xlabel('Ages')
pyplot.ylabel('Total Respondents')

pyplot.tight_layout()

pyplot.show()