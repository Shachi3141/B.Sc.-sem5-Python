print('hello world')
# Lennard Jons potentia
'''Lennard Jons potential energy function is use to describe the interaction
between two atoms.  
  where
       U is potential energy
       r is is dist. between two atom
       r0 is dist. between two atom where pot. energy is minimum 
       epsilon is depth of the potential well
       '''

import numpy as np
import matplotlib.pyplot as plt

r0 = 3  # in angstrom
e = 20  # in ev
r = np.arange(0.1, 10, 0.01)


def U(r):
    return e*((r0 / r) ** 12 - 2*(r0 / r) ** 6)


plt.plot(r, U(r))
plt.xlim(0, 8)
plt.ylim(-25, 50)
plt.axhline(0,ls='--')
plt.grid()
plt.title('LENNARD JONES POTENTIAL',color='b',size='20')
plt.xlabel('r---->',color='b',size='15')
plt.ylabel('U---->',color='b',size='15')
plt.show()
