import matplotlib.pyplot as plt
import numpy as np

def f(theta, phi, r):
    return r * np.sin(theta) * np.cos(phi)

theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 100)
r = np.linspace(0,2,100)

THETA, PHI, R = np.meshgrid(theta, phi, r)

X = R * np.sin(PHI) * np.cos(THETA)
Y = R * np.sin(PHI) * np.sin(THETA)
Z = R * np.cos(PHI)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
plt.show()