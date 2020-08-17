import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ClassPTC (4).csv')
veggies = data['Vegetable']
coffee= data['Coffee']

data_tt = data.loc[data['Genotype'] == 'tt']
data_TT = data.loc[data['Genotype'] == 'TT']

data_tt_veggies = data_tt['Vegetable']
data_TT_veggies = data_TT['Vegetable']

label=('tt', 'TT')

fig7, ax7 = plt.subplots()
ax7.set_title('Vegetable and Coffe Consumption of Students')
ax7.boxplot([data_tt_veggies, data_TT_veggies],labels= label) 

plt.show()

genotype = data['Genotype']
#for value in genotype:
    #if value == 'TT': 
       # value=0
    #elif value == 'Tt':
        #value= 1
    #elif value == 'tt':
        #value= 2
print(genotype)

label=('Coffee','Vegetables')
fig7, ax7 = plt.subplots()
ax7.set_title('Vegetable and Coffe Consumption of Students')
ax7.boxplot([coffee,veggies],labels= label) 

#plt.boxplot([genotype,veggies])

plt.show()