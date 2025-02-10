import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#creating a function to model and create data

def func(x,a,b,c):
	return a*np.exp(-(x-b)**2/(2*c**2))

#Generating clean data 
x=np.linspace(0,10,100)
y=func(x,1,5,2)

##Adding noise to the data
yn=y+0.2*np.random.normal(size=len(x))

#Executing curve_fit
popt,pcov = curve_fit(func,x,yn)

print(popt)

#Plotting
plt.scatter(x,yn)
plt.plot(x,y)
plt.show()
