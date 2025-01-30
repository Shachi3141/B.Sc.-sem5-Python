#Blackbody radiation

import numpy as np
import matplotlib.pyplot as plt

k=1.38*10**(-23)           #Boltzmann constant
c=3*10**8                  #speed of light in vaccum
h=6.626*10**(-34)          #plank constant
v=np.linspace(1,3e+13,1000)   #freq. for Plank
v1=np.linspace(1,3e+12,1000)  #freq. for Relaigh-Jeans

T1=100              #temprature
T2=120
#Relaigh-Jens law
def RJ(v1,T):
    return 8*(np.pi)*k*T*v1**2/c**3
#plot
plt.plot(v1,RJ(v1,T1),color='k',linestyle=':')
plt.plot(v1,RJ(v1,T2),color='k',linestyle='--')

#Plank law
def plnk(v,T):
    return (8*np.pi*h*(v**3)/c**3)*(np.exp((h*v)/(k*T))-1)**(-1)

#plot
plt.plot(v,plnk(v,T1),c='k',linestyle='-.')
plt.plot(v,plnk(v,T2),c='k')
plt.grid()
plt.xlabel('frequency------>',color='b')
plt.ylabel('spectral density----->',color='b')
plt.title('spectral density of blackbody radiation',color='k',fontweight='bold',size='16')
plt.legend(['Relaigh-Jeans law for T={}k'.format(T1),'Relaigh-Jeans law for T={}k'.format(T2),'Plank law for T={}k'.format(T1),'Plank law for T={}k'.format(T2)])
plt.show()
