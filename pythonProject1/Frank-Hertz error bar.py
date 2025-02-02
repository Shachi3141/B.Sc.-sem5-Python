# date 25/09/2023
# Frank Hertz exp
# I have 5 value from five data set
# 12.1,12.0,11.9,12.1,12.0

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])           #data set no
y = np.array([12.13, 11.97, 11.94, 12.15, 12.02]) #avarage value from different dataset
err= np.array([0.33,0.32 ,0.26,0.22,0.31])      #standered deviation corosponding data set
sum, sqsum = 0, 0
for i in range(len(y)):
    print(y[i])
    sum = sum + y[i]
    sqsum = sqsum + y[i] * y[i]
avg = sum / len(y)
sqavg = sqsum / len(y)
SD = np.sqrt(sqavg - (avg * avg))
print('SD=', SD, 'avg = ', avg)

print('error = ',err)

plt.errorbar(x,y,err,fmt='o-',capsize=3,label='error bar with one SD error')
plt.xlabel('data set no')
plt.ylabel('Excitation energy(ev)')
plt.title('FIRST EXCITATION ENERGY')
plt.legend()
plt.grid()
plt.ylim(9,15)
plt.xlim(0,6)
plt.show()