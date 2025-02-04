#specfic heat of a solid

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


T = np.linspace(0.1, 400, 1000)
TE = 100
TD = 125
T1 = TE / T
T2 = TD / T
R = 8.314
y = np.linspace(3 * R, 3 * R, 1000)

def f1(T):
    return 3 * R * ((T1) ** 2) * (np.exp(T1)) / (np.exp(T1) - 1) ** 2

def f2(x):
    return x ** 4 * np.exp(x) / (np.exp(x) - 1) ** 2

I = ([quad(f2, 0, t)[0] for t in T2])

def f3(T):
    return 9 * R * (1 / T2) ** 3 * I

plt.plot(T, y)
plt.plot(T, f1(T),linestyle='--')
plt.plot(T, f3(T))
plt.ylim(0,29)
plt.legend(['dulong-petit','einstein','debye'],loc='best')
plt.xlabel('temprature----->',color='b',size=17)
plt.ylabel('specfic heat----->',color='b',size=17)
plt.title('specfic heat of solid.',backgroundcolor='w',size=23)
plt.axhline()
plt.grid()
plt.show()
'''

#Comparing Duling-Petit law, Einstein law & Debye law for low temprature
import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(0.1, 40, 1000)
TE = 100
TD = 125
T1 = TE / T
T2 = TD / T
R = 8.314
y = np.linspace(3 * R, 3 * R, 1000)

def f1(T):
    return 3*R*(T1)**2*np.exp(-T1)

def f2(T):
    return (12/5)*R*(np.pi)**4 *(1/T2)**3

plt.plot(T,y,'k-',lw='2')
plt.plot(T,f1(T),'k--',lw='2')
plt.plot(T,f2(T),'k-.',lw='2')
plt.ylim(0,27)
plt.xlabel('temprature------>',color='b',size='17')
plt.ylabel('specfic heat----->',color='b',size='17')
plt.title('compresion at low temprature',color='b',size='23')
plt.legend(['dulong-petit','einstein','debye'],loc='best')
plt.show()
'''