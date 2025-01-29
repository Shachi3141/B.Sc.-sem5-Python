"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,100)

# Generate the first 10 Hermite polynomials
H = [np.poly1d([1])]
for n in range(1,10):
    H.append(np.poly1d([2*n,0])*H[n-1]-np.poly1d([2*n-2])*H[n-2])

# Plot the polynomials
plt.figure()
for i in range(5):
    plt.plot(x, H[i](x), label='H_%d(x)' % i)
plt.legend()
plt.show()

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)

# Generate the first few Hermite polynomials
H = [np.poly1d([1])]
for n in range(1, 6):
    H.append(np.poly1d([2 * n, 0]) * H[n - 1] - np.poly1d([2 * n - 2]) * H[n - 2])

# Create a figure with 2 rows and 3 columns of subplots
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

# Flatten the array of subplots
axs = axs.flatten()

# Plot the polynomials on each subplot
for i in range(6):
    axs[i].plot(x, H[i](x), label='H_%d(x)' % i)
    axs[i].set_title(f'H_{i}(x)')
    axs[i].set_xlabel('x')
    axs[i].set_ylabel('H_n(x)')
    axs[i].legend()

plt.show()
