import pandas as pd
from matplotlib import pyplot 

data = pd.read_csv('data2.csv')
ages= data['Age']
dev_salaries = data['All_Devs']
py_salaries= data['Python']
js_salaries= data['JavaScript']

pyplot.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

overall_median=57287

pyplot.plot(ages, py_salaries, label='Python')

pyplot.fill_between(ages,py_salaries,overall_median,where=(py_salaries > overall_median),interpolate= True,alpha=0.25)
pyplot.fill_between(ages,py_salaries,overall_median,where=(py_salaries <= overall_median),interpolate= True,alpha=0.25)

pyplot.legend()
pyplot.title('Median Salary (USD) by Age')
pyplot.xlabel('Ages')
pyplot.ylabel('Median Salary (USD)')
pyplot.tight_layout()

pyplot.show()