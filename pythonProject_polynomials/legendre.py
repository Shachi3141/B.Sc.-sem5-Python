import numpy as np
import matplotlib.pyplot as plt

# Define the degree of the polynomial
n = 3

# Create an array of x values between -1 and 1
x = np.linspace(-1,1,100)

# Evaluate the Legendre polynomial at the x values
legendre_poly = np.polynomial.legendre.legval(x, np.eye(n+1)[n])

# Plot the polynomial
plt.plot(x, legendre_poly, label='P_%d(x)' % n)
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.legend()
plt.show()
