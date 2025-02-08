
n=2
m=5
print(f"{m} is always grater than {n}")   #style of printing(f-string formatting)
#print("%d is always grater than %d"%n%m)  #<---- wrong only one variable is possible
print(m,'is always grater than',n)   #<---- you can write this
t=1.78234123
print(f"Default output gives t = {t}.") # as it is
print(f"We can set the precision: t = {t:.4}.") # upto 4-1=3 decimal point
print(f"Or control the number of decimals: t = {t:.2f}.") # upto two decimal point

#factorial of a given number
#08/11/21
#
n=int(input('give the number'))
n1=n
if n<0:
    print('please give a possitive number')
elif n==0:
    print('factorial 0 is 1')
else :

     sum1 = 1
     while (n > 0):
          sum1 *= n
          n -= 1
print("the factorial of", n1, 'is', sum1)



import numpy as np
import scipy as sc
import numpy.linalg as lin
from scipy.integrate import quad
from scipy.special import jn
from scipy.special import factorial
from scipy.integrate import odeint
a=np.matrix([[3,1],[2,2]])
b=lin.eigvals(a)
print(b)
f=lambda x : np.exp(-x**2)
p,q=quad(f,0,1)
print(p)
print(factorial(4))
print(jn(0,0))   #jn(n,x)
def f(x,t):
    dxdt=-k*x**2
    return dxdt
t=np.linspace(0,10,100)
k=1.0
x0=100
sol=odeint(f,x0,t)

def f1(x,t):
    dxdt=-k*x
    return dxdt
t=np.linspace(0,10,100)

sol1=odeint(f1,x0,t)

print(sol)
print(sol1)
import matplotlib.pyplot as plt

plt.plot(t,sol,label='given')
plt.plot(t,sol1,label='given1')
plt.show()


import numpy as np
import matplotlib.pyplot as plt

#plot and subplot
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
t1=np.arange(1,5,0.1)
print(f(t1))
t2=np.arange(1,5,0.01)
plt.figure()
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.xlabel('X----->',fontdict=font2)
plt.ylabel('Y----->',fontdict=font2)
plt.title('x vs e^x*cos(2*pi*x) graph',fontdict=font1)
plt.grid()
plt.legend(['line1','line2'])

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'r-.')

plt.xlabel('X----->',fontdict=font2)
plt.ylabel('Y----->',fontdict=font2)
plt.title('x vs cos(2*pi*x) graph',fontdict=font1,loc='left')
plt.grid(color = 'pink', linestyle = '--', linewidth = 1.5)

plt.show()


#add text in graph

x=np.linspace(-5,5,500)
y1=np.exp(-x**2/2)
y2=x*np.exp(-x**2/2)
y3=(np.exp(-x**2/2))-(2*x**2*(np.exp(-x**2/2)))
y4=x*np.exp(-x**2/2)-(2/3)*x**3*np.exp(-x**2/2)

plt.plot(x,y1,x,y2,x,y3,x,y4)
plt.title('wavefunctions in harmonic oscillator',loc='left')
plt.legend(['when N=0','when N=1','when N=2','when N=3'])
plt.show()
