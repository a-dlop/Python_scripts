# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:00:05 2022

@author: Daniel
"""
import numpy as np
import matplotlib.pyplot as plt

import scipy.special as sc

def distrbeta(x,alpha,beta):
    bet=1/sc.beta(alpha,beta)*x**(alpha-1)*(1-x)**(beta-1)
    return bet
alpha=500
beta=501
variables=alpha+beta-1
datos=list()
from datetime import datetime
#Método 1
startTime = datetime.now()


for i in range(variables):    
    U=np.random.rand(alpha+beta-1)
    p=np.partition(np.asarray(U), alpha)[alpha]
    datos.append(p)

plt.title("Comparación entre histograma distribucion beta metodo 1 y metodo 2" )
plt.hist(datos,density=True)    

#Python 3: 
print(datetime.now() - startTime)
#Método 2
startTime = datetime.now()

y1=np.random.gamma(alpha,scale=1,size=400)
y2=np.random.gamma(beta,scale=1,size=400)
Z=[y1[i]/(y2[i]+y1[i]) for i in range(len(y1))]
plt.hist(Z,alpha=0.5,density=True)
print(datetime.now() - startTime)


x=np.linspace(0,1,num=200)

disbeta=[distrbeta(i,alpha,beta) for i in x ]
plt.plot(x,disbeta)
plt.show()
