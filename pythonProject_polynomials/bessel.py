"""

import numpy as np

# Generate the first 10 Bessel polynomials
J = [np.poly1d([1])]
for n in range(1,10):
    J.append(np.poly1d([n,0])*J[n-1]-np.poly1d([n-1])*J[n-2])

# Print the polynomials
for i in range(10):


for i in range(5):
    plt.plot(x, J[i](x), label='J_%d(x)' % i)
plt.legend()
plt.show()

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)

# Generate the first 10 Bessel polynomials
J = [np.poly1d([1])]
for n in range(1,10):
    J.append(np.poly1d([n,0])*J[n-1]-np.poly1d([n-1])*J[n-2])

# Create a figure with 2 rows and 5 columns of subplots
fig, axs = plt.subplots(2, 5, figsize=(12, 8))

# Flatten the array of subplots
axs = axs.flatten()

# Plot the polynomials on each subplot
for i in range(10):
    axs[i].plot(x, J[i](x), label='J_%d(x)' % i)
    axs[i].set_title(f'J_{i}(x)')
    axs[i].set_xlabel('x')
    axs[i].set_ylabel('J_n(x)')
    axs[i].legend()

plt.show()
