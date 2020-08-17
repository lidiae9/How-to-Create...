import matplotlib
from matplotlib import pyplot

#comparing the average salary of developers based on age 
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] #these are the values on the x axis (age)

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752] #these are the values on the y axis (salary)

pyplot.plot(dev_x, dev_y) #this connects the y and x axis 

pyplot.title("Median Salary (USD) of Developers by Age") #gives the whole graph a title
pyplot.xlabel("Age")
pyplot.ylabel("Salary (USD)")

pyplot.show() #this shows the complete graph





#MAKING A GRAPH WITH TWO LINES - X AXIS STAYS THE SAME, TWO Y AXIS LINES
#COMPARING TWO Y VALUES TO THE CONSTANT X VALUES


age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] #these are the values on the x axis (age)

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752] #these are the values on the y axis (salary)
pyplot.plot(age_x, dev_y, label="All Developers") #this connects the y and x axis and you can also add a label so you know what they represent

#now we want to compare the values of python developers to normal developers - so we add another x and y axis values, but because
#the x-axis age values remain the same we can just feed that information into the plot with the new y axis values 
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640] #salary of python developers

pyplot.plot(age_x, py_dev_y, label="Python Developers")

#you can create a label like this pyplot.legen("[]") - but it needs to be in the same order that you fed the variables
pyplot.title("Median Salary (USD) of Developers by Age") #gives the whole graph a title
pyplot.xlabel("Age")
pyplot.ylabel("Salary (USD)")

pyplot.legend()
pyplot.show()

#For formatting the lines: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html 
#Website that gives you all the formatting codes: for color, linewidth, linestyle

#To add a grid: pyplot. grid(True)
#To tighten the graph so it's not wonky on a small screen: pyplot.tight_layout()