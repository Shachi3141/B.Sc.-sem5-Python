
#solve the equation for driven demped pendulam.given equation is
#d20/dt2=(1/q)(d0/dt)+sin0+pcos(omg*t)
#in this problem i take 0(theta) as y and d0/dt as z

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#value given
q = 2.0
p = 1.5
omg = 0.65

def dampen(u, t):    #function
    y, z = u
    dydt = z
    dzdt = (z / q) + np.sin(y) + p * np.cos(omg * t)
    return np.array([dydt, dzdt])


u0 = [0, 0]   #initial condition
t = np.linspace(0, 18, 100)
sol = odeint(dampen, u0, t)
y = sol[:, 0]    #angular displacement
z = sol[:, 1]    #angular velotity

plt.plot(t, y)
plt.title('angular displacement vs time graphg',size='15',color='b')
plt.xlabel('time----->')
plt.ylabel('angular displacement----->')
plt.show()

import numpy as np

'''
#question 3
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import hermite

x=np.arange(-5,5,0.01)

#loop for psi
plt.figure(figsize=(10,10))
for n in range(5):
    hn=hermite(n)
    psi=(1/np.sqrt((2**n)*math.factorial(n)))*(hn(x))*np.exp(-(x*x)/2)
    plt.plot(x,psi,lw=2,ls='-')
plt.title('wavefunction in simple harmonic oscillator',size='15')
plt.xlabel('x----->',size='15')
plt.ylabel('$\psi_n(x)$----->',size='15')
plt.legend(['when n=0','when n=1','when n=2','when n=3','when n=4'])
plt.grid()
plt.show()

#loop for psi*psi
plt.figure(figsize=(10,10))
for n in range(5):
    hn=hermite(n)
    psi=(1/np.sqrt((2**n)*math.factorial(n)))*(hn(x))*np.exp(-(x*x)/2)
    plt.plot(x,psi*psi,lw=1,ls='-')
plt.title('probablity density in simple harmonic oscillator',size='15')
plt.xlabel('x----->',size='15')
plt.ylabel('$|\psi_n(x)|^2$----->',size='15')
plt.legend(['when n=0','when n=1','when n=2','when n=3','when n=4'])
plt.grid()
plt.show()

'''

#question4

import numpy as np
import matplotlib.pyplot as plt

a=1
x=np.arange(0,15,0.01)
R10=2*a**(-3/2)*np.exp(-x/a)
R20=(1/np.sqrt(2))*a**(-3/2)*(1-(x/2*a))*np.exp(-x/2*a)
R21=(1/2*np.sqrt(6))*a**(-3/2)*(x/a)*np.exp(-x/2*a)
R30=(2/3*np.sqrt(3))*a**(-3/2)*(1-(2*x/3*a)+((2*x*x)/(27*a*a)))*np.exp(-x/3*a)
R31=(8/27*np.sqrt(6))*a**(-3/2)*(1-(x/6*a))*(x/a)*np.exp(-x/3*a)
R32=(4/81*np.sqrt(30))*a**(-3/2)*((x*x)/(a*a))*np.exp(-x/3*a)

plt.figure(figsize=(10,8))
plt.subplot(3,1,1)
plt.grid()
plt.title('radial probablity density for the electron in hydrogen atom when n=1',size='11')
plt.plot(x,x*x*R10*R10)
plt.legend(['R10*R10'])

plt.subplot(3,1,2)
plt.grid()
plt.title('radial probablity density for the electron in hydrogen atom when n=2',size='11')
plt.plot(x,x*x*R20*R20,x,x*x*R21*R21)
plt.legend(['R20*R20','R21*R21'])

plt.subplot(3,1,3)
plt.grid()
plt.title('radial probablity density for the electron in hydrogen atom when n=3',size='11')
plt.plot(x,x*x*R30*R30,x,x*x*R31*R31,x,x*x*R32*R32)
plt.legend(['R30*R30','R31*R31','R32*R32'])
plt.tight_layout()
plt.show()


a=(2,3,4,5,6,7,8,9)
print(a)
for i in range(len(a)):
    if a[i] == 5:
        j=i
        break
    else :
        #print(i)
        j=0
print(j)


x =np.matrix()
print(x[:, 3])
