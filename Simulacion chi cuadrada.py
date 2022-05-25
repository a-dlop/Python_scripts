# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:26:07 2022

@author: Daniel
"""
import numpy as np
import matplotlib.pyplot as plt
import math
U_1=np.random.rand(1000000)
U_2=np.random.rand(1000000)
z=np.arange(0, 10)
p=1/2*np.exp(-z/2)
x=[ math.sqrt(-2*math.log(U_1[i]))*math.cos(2*math.pi*U_2[i]) for i in range( len(U_1))]
y=[ math.sqrt(-2*math.log(U_1[i]))*math.cos(2*math.pi*U_2[i]) for i in range( len(U_1))]
xsquare=np.square(x)
ysquare=np.square(y)
x2=xsquare+ysquare
plt.title("Comparación entre histograma y distribucion chi cuadrada")
plt.hist(x2,bins=100,range= [0,20],density=True)
plt.plot(z,p)

"""
#Graficas para comprobar que se distribuyen normal
plt.hist(x,bins=100,label='Variable X',density=True)
plt.hist(y,bins=100, label='Variable y',density=True, alpha=0.5)
plt.show()"""