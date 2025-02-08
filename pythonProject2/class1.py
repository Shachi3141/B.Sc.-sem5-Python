#a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(a[2:7:2])
#print(a[1:])
'''
# initial_index:final:incriment
print(a)
print(a[:5:1]) initial is defolt
print(a[1:])    final and incriment is defolt
print(a[::2])   initial and final is defolt
'''

'''
b = list(range(1, 9))
print(b)
print(list(range(23,70,5)))
print([i*i for i in range(10)])    #notice[] and writting formate
c=[k*5 for k in [5,6,7,8]]
print(c)
c.insert(2,33)
print(c)


'''
'''
a=[2,1,3,4,3,4,5,6,7,3,4,2,1,4]
print(len(a))

l=[ut for ut in range(10)]
m=list(range(10))
n=list(range(0,10,2))
print(l,m,n)
print([i*i for i in range(5)])
print([k*3 for k in [2,4,3]])
print([character for character in 'python'])
print([[j,k] for j in range(4) for k in range(j+1,4)])
print([s for s in ["blue","red","green","yellow","beize"]])
print([p for p in ["blue","red","green","yellow","beize"] if "l" in p])
d=[s for s in ["blue","red","green","yellow","beize"]]
print(d[0:2])
print([p[1] for p in ["blue","red","green","yellow","beize"] if "l" in p])
mean_a=sum(a)/len(a)
print(mean_a)
del d[3]
print(d)
d.remove('red')
print(d)
d.append('asd')
print(d)
d.insert(0,'dsa')
print(d)
print(a)
g=sorted(a,reverse=True)  # <---- notice capital 'T'
print(g)
a.reverse()
print(a)
print(d)
d.sort()
print(d)

'''
'''
a = (1, 2, 3, 4, 4, 5)
b=2,3,1,4,5,3,2    #tuple
print(type(a))
print(a)
v1=[2,3,4]
v2=[3,4,5]   #list

print(len(v1))
v3=[0,0,0]
for i in range(len(v1)):
 print(v1[i]+v2[i],end='')
 v3[i]=v1[i]+v2[i]
mat=[v1, v2, v3]
print(v3,'\n')
print(mat)
print(mat[1][2])

'''
# to the fibonacci series upto a given number n
# 5 nov 2021 , 10:20
# @author: python group vb
#
'''
n=50    #int(input("please enter an integer"))
print(n)
def fib(n):
    l=[]
    a,b=0,1
    while a<n :
        #print(a,' ',end='')
        l.append(a)
        a,b=b,a+b
    return(l)
print( '\n the fibonacci series up to %d is'%n,fib(n) )
c=fib(20)
print(c)
'''

'''
# sum of natural numbers
#08/11/21
# modification:

n=int(input('give the number'))
#n=10
n1=n
if n<0:
    print('please enter a possitive number')
else:
    def sumn(n):
        sum1 = 0
        while(n>0) :
           sum1 += n
           n -= 1
        print("the sum of natural no. upto", n1,'is', sum1)
    sumn(n)

'''
'''
import numpy as np
import matplotlib.pyplot as plt

# Given data
distance = [2.890371758,2.995732274,3.091042453,3.17805383,3.258096538,3.33220451,3.401197382,3.465735903,3.526360525]
current = [1.902107526, 1.658228077, 1.410986974, 1.178654996, 1.011600912, 0.875468737, 0.741937345, 0.615185639, 0.500775288]

# Plotting the distance vs current graph
plt.plot(distance, current, marker='o', linestyle='-')

# Adding labels and title
plt.xlabel('Log of Distance')
plt.ylabel('Log of Current')
plt.title('Distance vs Current Graph')

# Display the plot
plt.grid(True)
plt.show()
'''

