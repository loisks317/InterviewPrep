#
# bobAmoeba.py
#
# Insight July, 2016
#
import numpy as np

#
#
n=1000
cap = 20
population = 1
deadCount=0
AliveCount=0


for ii in range(n):
    population = 1
    for jj in range(cap):
        newpopulation=np.zeros(population)
        choice=np.random.rand(population)
        newpopulation[choice<=0.25]=1
        newpopulation[choice>=0.5]=2
        # don't need the zero population, already zero
        population = int(np.sum(newpopulation))
        if population == 0:
            deadCount+=1
            break #  breaks out of for loop
    if population > 0:
        AliveCount+=1

print deadCount/(1.0*(deadCount+AliveCount))
# should be 0.5 
