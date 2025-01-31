# plot the following energy distribution function
# 1.maxwell-boltzmann 2.fermi-dirac 3.bose-einstein

import numpy as np
import matplotlib.pyplot as plt

mu = 0                # chemicl potential
k = 1.38 * 10 ** -23  # Boltzmann constant
e = 1.6e-19           #electronic charge
E = np.linspace(-0.5, 0.5, 1000) #energy range in ev

#general function define
def F(E, T,a):
    return (np.exp((E - mu) *e /( k* T) )+a)**-1

#Maxwell-Boltzmann ploting
plt.plot(E,F(E,500,0),ls='-',lw='2',c='k')
plt.plot(E,F(E,1000,0),ls='--',lw='2',c='k')
plt.plot(E,F(E,1500,0),ls='-.',lw='2',c='k')
plt.plot(E,F(E,2000,0),ls=':',lw='2.5',c='k')
plt.grid()
plt.ylim(0,1)
plt.xlim(0,0.5)
plt.legend(['temp=500k','temp=1000k','temp=1500k','temp=2000k'])
plt.title('Maxwell-Boltzmann distribution',color='b',size='23')
plt.xlabel('energy(in ev)---->',color='b',size='17')
plt.ylabel('M-B dist. function---->',color='b',size='17')
plt.show()

#Fermi-Dirac ploting
plt.plot(E,F(E,500,1),ls='-',lw='2',c='k')
plt.plot(E,F(E,1000,1),ls='--',lw='2',c='k')
plt.plot(E,F(E,1500,1),ls='-.',lw='2',c='k')
plt.plot(E,F(E,2000,1),ls=':',lw='2.5',c='k')
plt.grid()
plt.ylim(0,1)
plt.xlim(-0.5,0.5)
plt.legend(['temp=500k','temp=1000k','temp=1500k','temp=2000k'])
plt.title('Fermi-Dirac distribution',color='b',size='23')
plt.xlabel('energy(in ev)---->',color='b',size='17')
plt.ylabel('F-D dist. function---->',color='b',size='17')
plt.show()

#Bose-Einstein ploting
plt.plot(E,F(E,500,-1),ls='-',lw='2',c='k')
plt.plot(E,F(E,1000,-1),ls='--',lw='2',c='k')
plt.plot(E,F(E,1500,-1),ls='-.',lw='2',c='k')
plt.plot(E,F(E,2000,-1),ls=':',lw='2.5',c='k')
plt.grid()
plt.ylim(0,20)
plt.xlim(0,0.3)
plt.legend(['temp=500k','temp=1000k','temp=1500k','temp=2000k'])
plt.title('Bose-Einstein distribution',color='b',size='23')
plt.xlabel('energy(in ev)---->',color='b',size='17')
plt.ylabel('B-E dist. function---->',color='b',size='17')
plt.show()

#compare this three distribution for a fixt temprature
plt.plot(E,F(E,500,0),ls='-',lw='2',c='k')
plt.plot(E,F(E,500,1),ls='--',lw='2',c='k')
plt.plot(E,F(E,500,-1),ls='-.',lw='2',c='k')
plt.grid()
plt.text(0.15,0.2,'For temprature=500k')
plt.xlim(0,0.3)
plt.ylim(0,0.5)
plt.legend(['maxwell-boltzmann','fermi-dirac','bose-einstein'])
plt.title('compare three distribution for a fixt temprature',color='b',size='20')
plt.xlabel('energy(in ev)---->',color='b',size='15')
plt.ylabel('B-E dist. function---->',color='b',size='15')
plt.show()
