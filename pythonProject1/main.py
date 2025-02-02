#Maxwell speed distribution

import numpy as np
import matplotlib.pyplot as plt
N=6.022* 10**23
k=1.38* 10**-23
m=1.67* 10**-22
v=np.arange(0.01,100,0.1)

def Fm(v,T):
    a=(m/(2*k*T))
    return 4*np.pi*N*(a/np.pi)**(3/2)*(np.exp(-(a*v**2)))*v**2


plt.plot(v,Fm(v,200),ls='-',lw='2',c='k')
#plt.plot(v,Fm(v,600),ls='--',lw='2',c='k')
#plt.plot(v,Fm(v,1000),ls='-.',lw='2',c='k')
#plt.plot(v,Fm(v,1400),ls=':',lw='2',c='k')
plt.legend(['temp=200k','temp=600k','temp=1000k','temp=1400k'],loc='best')
plt.title('Maxwell speed distribution',color='b',size='23')
plt.xlabel('speed(v)---->',color='b',size='17')
plt.ylabel('dist. function---->',color='b',size='17')
plt.xlim(0,40)
plt.axhline(0,ls='--')
plt.grid()

plt.fill_between(v,Fm(v,200),color='m',alpha=.3)

val=Fm(v,200)
print(max(val))
for i in range(len(val)):
    if val[i]==max(val):
        j=i
        break
print(j)
plt.plot(v[j],val[j],marker='o',color='b')
plt.show()
print(v[j],val[j])




