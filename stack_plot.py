import matplotlib
from matplotlib import pyplot

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

legends=['player1','player2','player3']

pyplot.stackplot(minutes,player1,player2,player3,labels=legends)

#to change location of the legend you can input loc= "sting" 
pyplot.legend(loc='upper left')
pyplot.show()


days = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dev1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
dev2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
dev3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

legends2= ['developer1','developer2', 'developer3']

pyplot.stackplot(days,dev1,dev2,dev3,labels=legends2)
pyplot.legend(loc='lower left')

pyplot.show()

