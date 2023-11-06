import math as mt
import numpy as np
import scipy as sc
import scipy.integrate as integrate
import scipy.stats as stat
###########################################################  1  ###########################################################

def binomial_dist(P,N,n):
    return mt.factorial(N)/(mt.factorial(n)*mt.factorial(N-n))*(P)**n*(1-P)**(N-n)

median = 45
dataX = [35.5,44.5,39.8,33.3,51.4,51.3,30.5,48.9,42.1,40.3,52.4,59.8,42.8,42.6,65.4,39.3,36.8,40.1,38.0,46.8,26.2,60.9,45.6,27.1,47.3,36.6,55.6,45.1,52.2,43.5]
dataY = median*np.ones_like(dataX)

dataZ = dataY-dataX

#We formulate an hipothesis that states the mean and median of Z is 0
#this states that the number of negatives = positives

p=0
n=0
for i in dataZ:
    if i<0:
        n+=1
    elif i>0:
        p+=1

if n==p:
    print("Median is 45")
else:
    print("Positive:",p)
    print("Negative:",n)

pvalue=binomial_dist(0.5,30,n)

print("p-value:",pvalue)

sta,pval=stat.wilcoxon(dataX,dataY)
stax,pvalX=stat.wilcoxon(dataX)

print(pval,pvalX)

