#Python code for Partition function for two level system:

import numpy as np
import matplotlib.pyplot as plt
u=9.24e-27 # J/Tesla v taking Bohr magneton
B=1
k=1.38e-23
T=np.linspace(0.1,3,1000)
N=2
def par(T):
    a=np.exp((u*B)/(k*T))
    b=np.exp(-(u*B)/(k*T))
    return a+b
zn=par(T)**N
plt.plot(T,zn,'k',label='$Z_N$')
plt.xlabel('------>Temperature(in K)',size='17')
plt.ylabel('----->Partition function $ Z_N$',size='17')
plt.title('Partion function of N=4 Spin half particle',{'weight':'black'},size='19')
plt.legend(loc='best', fontsize='14')
plt.grid()
plt.show()

#Python code for Magnetisation and Susceptibility for two level system:

#import numpy as np
#import matplotlib.pyplot as plt
u=1
B=1
k=1
n=6.022e23 #taking 1 mole particle
T=np.linspace(0.01,5,1000)
M=n*u*np.tanh(u*B/(k*T))
plt.plot(T,M,'k')
plt.xlabel("--->Temperature T",size='17')
plt.ylabel("--->Magnetisaton,M (A/m)",size='17')
plt.title('Magnetisaton for Two-level system',{'weight':'black'},size='19')
plt.grid()
plt.show()

#for low temperature
T1=np.linspace(0.1,10,1000)
m1=n*u*(T1/T1)
plt.plot(T1,m1,'k')
plt.xlabel("--->Temperature,T (in K)",size='17')
plt.ylabel("--->Magnetisation,M (A/m)",size='17')
plt.title("Magnetisation for low temperature",{'weight':'black'},size='19')
plt.grid()
plt.show()

#for high temperature
T2=np.linspace(150,500,1000)
m2=(n*(u**2)*B)/(k*T2)
plt.plot(T2,m2,'k')
plt.xlabel("--->Temperature,T (in K)",size="17")
plt.ylabel("--->Magnetisation,M (A/m)",size='17')
plt.title("Magnetisation for high temperature (Curie law)",{'weight':'black'},size='19')
plt.grid()
plt.show()

#Curie law and Susceptibility
x=(n*u**2)/(k*T2)
plt.plot(T,x,'k')
plt.xlabel("--->Temperature,T (in K)",size='18')
plt.ylabel("--->Suceptibility ($\chi$)",size='15')
plt.title("Curie Law",{'weight':'black'},size='19')
plt.grid(color='#d3d3d3')
plt.xticks(fontsize='15')
plt.yticks(fontsize='15')
plt.tight_layout()
#plt.show()

