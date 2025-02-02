import matplotlib.pyplot as plt
import numpy as np

beta=.9
def f(theta, phi):
    S=np.sin(theta)
    C=np.cos(phi)
    F_d=(1-beta*C)
    return  ((S**2)/(F_d)**5)

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)

THETA, PHI = np.meshgrid(theta, phi)
R = f(THETA, PHI)

X = R * np.sin(PHI) * np.cos(THETA)
Y = R * np.sin(PHI) * np.sin(THETA)
Z = R * np.cos(PHI)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()