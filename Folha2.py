import math as mt
import numpy as np
import scipy as sc
import scipy.integrate as integrate

###########################################################  1  ###########################################################
print("Exercise 1")
N=25
R=5
P=0.1

def binomial_dist(P,N,n):
    return mt.factorial(N)/(mt.factorial(n)*mt.factorial(N-n))*(P)**n*(1-P)**(N-n)

########### a) #############

i=0
for n in range(0,R+1):
    i+=binomial_dist(P,N,n)
print("a) 5 or less have kidney problems:",i)

########### b) #############

print("b) 6 or more have kidney problems",1-i)

########### c) #############

i=0
for n in range(6,10):
    i+= binomial_dist(P,N,n)
print("c) Between 6 and 9 have kidney problems:",i)

########### c) #############

i=0
for n in range(2,5):
    i+= binomial_dist(P,N,n)
print("d) 2, 3 or 4 have kidney problems:",i)



###########################################################  2  ###########################################################

print("Exercise 2")

N=13
P=0.9

########### a) #############

n=7
i=binomial_dist(P,N,n)
print("a) Exactly 7:",i)

########### b) #############

n=6
i=binomial_dist(P,N,n)
print("b) Exactly 6:",i)

########### c) #############

R=8
i=0
for n in range(0,R):
    i+=binomial_dist(P,N,n)
print("c) Greater than 7:",1-i)

########### d) #############

R=8
i=0
for n in range(0,R+1):
    i+=binomial_dist(P,N,n)
print("d) No more than 8:",i)

########### e) #############

i=0
for n in range(4,12):
    i+=binomial_dist(P,N,n)
print("e) Between 4 and 11:",i)

########### f) #############

R=10
i=0
for n in range(0,R):
    i+=binomial_dist(P,N,n)
print("f) Not less than 10:",1-i)

########### g) #############

R=round(N/2)+1
i=0
for n in range(R,N+1):
    i+=binomial_dist(P,N,n)
print("g) Greater than the number of people who do not improve:",i)


###########################################################  3 ################################################
print("Exercise 3")
lam=13

def poisson_dist(l,k):
    return mt.exp(-l)*l**k/mt.factorial(k)

########### a) ##############

Prob = poisson_dist(lam,10)
print("a) Exactly 10:",Prob)

########### b) ##############

Prob=0
R=8
for n in range(0,R):
    Prob += poisson_dist(lam,n)
print("b) At least 8:",1-Prob)


########### c) ##############

Prob=0
R=12
for n in range(0,R+1):
    Prob += poisson_dist(lam,n)
print("c) No more than 12:",Prob)

########### d) ##############

Prob=0
R=7
for n in range(0,R):
    Prob += poisson_dist(lam,n)
print("d) Less than 7:",Prob)

########### e) ##############

Prob=0
for n in range(9,16):
    Prob += poisson_dist(lam,n)
print("e) Between 9 and 15:",Prob)

############################################################  4 ################################################
print("Exercise 4")

mean=60
dev=12

def normal_dist(dev,mean,x):
    return mt.exp(-0.5*(x-mean)**2/dev**2)/(dev*mt.sqrt(2*mt.pi))

mi=0

def prob_normal(dev,mean,mi,mf):
    Prob=integrate.quad(lambda x: normal_dist(dev,mean,x),mi,mf)
    return Prob[0]

########### a1) ##############

print("a1) Exactly 60:",0)

########### a2) ##############

m=70
Prob=prob_normal(dev,mean,mi,m)
print("a2) More than 70 Kg:",1-Prob)

########### a3) ##############

m=54
Prob=prob_normal(dev,mean,mi,m)
print("a3) 54 Kg or less:",Prob)

########### a4) ##############

mi=55
mf=65

Prob=prob_normal(dev,mean,mi,mf)
print("a4) Between 55 Kg and 65 Kg:",Prob)


########### a5) ##############

print("a5) Maximum 60 Kg:",0.5)


###########  b) #############

def find_x_given_prob(Probf,mi,mf):
    Prob=0
    while True: 
        Prob+=prob_normal(dev,mean,mi,mf)
        if  0< abs(Prob-Probf) < 0.00001:
            return mf
        else:
            mi=mf
            mf+=0.0001

###########  b1) #############

mi=0
mf=mean
Probf=0.75
print("b1) The x at which the Prob=0.75:",find_x_given_prob(Probf,mi,mf))

###########  b1) #############

mi=0
Probf=0.1539
rule=[34.1,34.1+13.6,34.1+13.6+2.1]
for n in range(0,len(rule)+1):
    if Probf<0.5:
        r=(0.5-Probf)-rule[n]/100
        if  r > 0:
            mf=mean-(n+1)*dev
        elif r < 0:
            break
print(mf)

print("b2) The x at which the Prob=0.1539:",find_x_given_prob(Probf,mi,mf))


############################################################  5 ################################################
print("Exercise 5")

mean=170
dev=24

###########   a)    #########

###########   a1)    #########

print("Exactly 170 g:",0)

###########   a2)    #########

mi=160
mf=180
Prob=prob_normal(dev,mean,mi,mf)
print("Exactly 170 g:",Prob)



