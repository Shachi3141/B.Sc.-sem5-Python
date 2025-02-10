#curve fitting f(x)=ax+b
import numpy as np
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

#creating a function to model and create dat
def func(x,a,b):
	return a*x +b

#Generating clean data
x=np.linspace(0,10,100)
y=func(x,1,2)

#Adding noise to the data
yn=y+0.9 * np.random.normal(size=len(x))

#Executing curve_fit no noisy data
popt, pcov = curve_fit(func, x,yn)

#popt returns the best fit values for parameters
#of the given model (func).

print(popt)

plt.scatter(x,yn)
plt.plot(x,y,'r')
plt.show()
