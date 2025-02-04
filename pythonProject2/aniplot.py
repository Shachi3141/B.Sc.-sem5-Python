import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


'''
# Sample data
t = np.linspace(0, 10, 100)
z = np.sin(t)
z2 = np.cos(t)

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

# Create initial scatter and line plot
scat = ax.scatter([], [])
line2, = ax.plot([], [], lw=2)

def update(frame):
    x = t[:frame]
    y = z[:frame]
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return (scat, line2)

# Create animation
ani = FuncAnimation(fig, update, frames=len(t), blit=True)

# Display the animation
plt.show()
'''

'''
## question 2   part 1 Planetary motion using Rungi Kutta 4

#Value of A nad B
A = 2
B = 3

def f1(t,r,v,Th):  #drdt
    return v
def f2(t,r,v,Th):   #dvdt
    return (B ** 2 / r ** 3) - (A / r ** 2)
def f3(t,r,v,Th):   #dThdt
    return B / r ** 2

# initial condition r(0)=b=3.5, V(0)=0,Th(0)=0
r0 = 3.5
v0 = 0
Th0 = 0
t=0
r_0=r0 #ignore this
i=0
#create list to store new value inside loop
r_a=[r0]
v_a=[v0]
Th_a=[Th0]
t_a=[t]

#Step size
step_size=0.1
h= step_size
#Loop for Rk4 method
while Th0 < (4*np.pi) :
    k1 = h * f1(t,r0,v0,Th0)
    m1 = h * f2(t,r0,v0,Th0)
    l1 = h * f3(t,r0,v0,Th0)

    k2 = h * f1(t + h / 2, r0 + k1 / 2, v0 + m1 / 2,Th0 + l1 / 2)
    m2 = h * f2(t + h / 2, r0 + k1 / 2, v0 + m1 / 2,Th0 + l1 / 2)
    l2 = h * f3(t + h / 2, r0 + k1 / 2, v0 + m1 / 2,Th0 + l1 / 2)

    k3 = h * f1(t + h / 2, r0 + k2 / 2, v0 + m2 / 2,Th0 + l2 / 2)
    m3 = h * f2(t + h / 2, r0 + k2 / 2, v0 + m2 / 2,Th0 + l2 / 2)
    l3 = h * f3(t + h / 2, r0 + k2 / 2, v0 + m2 / 2,Th0 + l2 / 2)

    k4 = h * f1(t + h, r0 + k3, v0 + m3,Th0 + l3)
    m4 = h * f2(t + h, r0 + k3, v0 + m3,Th0 + l3)
    l4 = h * f3(t + h, r0 + k3, v0 + m3,Th0 + l3)
    r = r0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    v = v0 + (m1 + 2 * m2 + 2 * m3 + m4) / 6
    Th =Th0 + (l1 + 2 * l2 + 2 * l3 + l4) / 6
    t = t + h
    #print
  #  print("{:15.8f}  {:15.8f}  {:15.8f}  {:15.8f}".format(t, r, v, Th))

    r_a .append(r)
    v_a .append(v)
    Th_a .append(Th)
    t_a .append(t)

    #update
    r0=r
    v0=v
    Th0=Th
    # To prevent extremely bigger loop
    i += 1
    if (i > 100000):
        print("<NOT COMPLETE> increase stepsize(machine also get tired) ")
        break
    #loop end



print('Number of full rotation', Th / (2 * np.pi))  #no of rotation= final theta/2 pi
#Highlight some special points
plt.scatter(0, 0, color='r')                        # Point at origin
plt.scatter(r_0 * np.cos(0), r_0 * np.sin(0),c='k') #point at initial position
plt.scatter(r * np.cos(Th), r * np.sin(Th),c='b')   #point at final position
#Measurement stationary orbit ## checking only radial separation
## bcause we know angular one(condition of loop is on angle )
print('radial separation between initial and final point',np.abs(r-r_0))
print(len(t_a))

fig, ax = plt.subplots()
#scat = ax.scatter([], [])
line2, = ax.plot([], [], lw=2)

def update(frame):
    x = r_a[:frame] * np.cos(Th_a[:frame])
    y = r_a[:frame] * np.sin(Th_a[:frame])
    line2.set_xdata(x)
    line2.set_ydata(y)
    return ( line2)

# Create animation
ani = FuncAnimation(fig, update, frames=len(t_a), blit=True)

# Display the animation
plt.show()


#Trajectory plot
plt.plot(r_a * np.cos(Th_a), r_a * np.sin(Th_a))
plt.title('trajectory of motion')
plt.grid()
plt.show()
'''



'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
A = 2
B = 3

# Differential equations
def f1(t, r, v, Th):  # dr/dt
    return v

def f2(t, r, v, Th):  # dv/dt
    return (B ** 2 / r ** 3) - (A / r ** 2)

def f3(t, r, v, Th):  # dTh/dt
    return B / r ** 2

# Initial conditions
r0 = 3.5
v0 = 0
Th0 = 0
t = 0

# Lists to store the results
r_a = [r0]
v_a = [v0]
Th_a = [Th0]
t_a = [t]

# Step size
step_size = 0.1
h = step_size

# Runge-Kutta 4th order method
while Th0 < (2 * np.pi):
    k1 = h * f1(t, r0, v0, Th0)
    m1 = h * f2(t, r0, v0, Th0)
    l1 = h * f3(t, r0, v0, Th0)

    k2 = h * f1(t + h / 2, r0 + k1 / 2, v0 + m1 / 2, Th0 + l1 / 2)
    m2 = h * f2(t + h / 2, r0 + k1 / 2, v0 + m1 / 2, Th0 + l1 / 2)
    l2 = h * f3(t + h / 2, r0 + k1 / 2, v0 + m1 / 2, Th0 + l1 / 2)

    k3 = h * f1(t + h / 2, r0 + k2 / 2, v0 + m2 / 2, Th0 + l2 / 2)
    m3 = h * f2(t + h / 2, r0 + k2 / 2, v0 + m2 / 2, Th0 + l2 / 2)
    l3 = h * f3(t + h / 2, r0 + k2 / 2, v0 + m2 / 2, Th0 + l2 / 2)

    k4 = h * f1(t + h, r0 + k3, v0 + m3, Th0 + l3)
    m4 = h * f2(t + h, r0 + k3, v0 + m3, Th0 + l3)
    l4 = h * f3(t + h, r0 + k3, v0 + m3, Th0 + l3)

    r = r0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    v = v0 + (m1 + 2 * m2 + 2 * m3 + m4) / 6
    Th = Th0 + (l1 + 2 * l2 + 2 * l3 + l4) / 6
    t += h

    r_a.append(r)
    v_a.append(v)
    Th_a.append(Th)
    t_a.append(t)

    # Update variables for next iteration
    r0 = r
    v0 = v
    Th0 = Th

# Output results
print('Number of full rotations:', Th / (2 * np.pi))  # Number of rotations
print('Radial separation between initial and final point:', np.abs(r - r0))
print('Number of time steps:', len(t_a))


# Animation setup
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
line2, = ax.plot([], [], lw=2)

def update(frame):
    x = r_a[:frame] * np.cos(Th_a[:frame])
    y = r_a[:frame] * np.sin(Th_a[:frame])
    line2.set_data(x, y)
    return line2,

# Create animation
ani = FuncAnimation(fig, update, frames=len(t_a), blit=True)

# Display the animation
plt.show()

'''



#This code is speed up the animation


# Constants
A = 2
B = 3

# Differential equations
def f1(t, r, v, Th):  # dr/dt
    return v

def f2(t, r, v, Th):  # dv/dt
    return (B ** 2 / r ** 3) - (A / r ** 2)

def f3(t, r, v, Th):  # dTh/dt
    return B / r ** 2

# Initial conditions
r0 = 3
v0 = 0
Th0 = 0
t = 0

# Lists to store the results
r_a = [r0]
v_a = [v0]
Th_a = [Th0]
t_a = [t]

# Step size
step_size = 0.1
h = step_size

# Runge-Kutta 4th order method
while Th0 < (4 * np.pi):
    k1 = h * f1(t, r0, v0, Th0)
    m1 = h * f2(t, r0, v0, Th0)
    l1 = h * f3(t, r0, v0, Th0)

    k2 = h * f1(t + h / 2, r0 + k1 / 2, v0 + m1 / 2, Th0 + l1 / 2)
    m2 = h * f2(t + h / 2, r0 + k1 / 2, v0 + m1 / 2, Th0 + l1 / 2)
    l2 = h * f3(t + h / 2, r0 + k1 / 2, v0 + m1 / 2, Th0 + l1 / 2)

    k3 = h * f1(t + h / 2, r0 + k2 / 2, v0 + m2 / 2, Th0 + l2 / 2)
    m3 = h * f2(t + h / 2, r0 + k2 / 2, v0 + m2 / 2, Th0 + l2 / 2)
    l3 = h * f3(t + h / 2, r0 + k2 / 2, v0 + m2 / 2, Th0 + l2 / 2)

    k4 = h * f1(t + h, r0 + k3, v0 + m3, Th0 + l3)
    m4 = h * f2(t + h, r0 + k3, v0 + m3, Th0 + l3)
    l4 = h * f3(t + h, r0 + k3, v0 + m3, Th0 + l3)

    r = r0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    v = v0 + (m1 + 2 * m2 + 2 * m3 + m4) / 6
    Th = Th0 + (l1 + 2 * l2 + 2 * l3 + l4) / 6
    t += h

    r_a.append(r)
    v_a.append(v)
    Th_a.append(Th)
    t_a.append(t)

    # Update variables for next iteration
    r0 = r
    v0 = v
    Th0 = Th

# Sample data to reduce number of frames
sampling_rate = 10  # Adjust this to control the speed
r_a_sampled = r_a[::sampling_rate]
Th_a_sampled = Th_a[::sampling_rate]

# Animation setup
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
line2, = ax.plot([], [], lw=2)
point, = ax.plot([], [], 'bo')  # Point marker

ax.scatter(0, 0, color='r')

def update(frame):
    x = r_a_sampled[:frame] * np.cos(Th_a_sampled[:frame])
    y = r_a_sampled[:frame] * np.sin(Th_a_sampled[:frame])
    line2.set_data(x, y)
    point.set_data(x, y)  # Update point position
    return line2,point

# Create animation with increased interval
ani = FuncAnimation(fig, update, frames=len(r_a_sampled), interval=50, blit=True)

writer = animation.PillowWriter(fps=15)
ani.save('scatter.gif', writer=writer)
# Display the animation
plt.show()
















'''
def f(t, n):
    x = np.sin( t)
    y = np.cos( t)
    return x, y


t = np.arange(0, 20, 1)
n = np.arange(0,20,0.1)
z = f(t,1)

x = z[0]
y = z[1]
#print(z)

lines1 = plt.plot(t,x)
lines2 = plt.plot(t,y)
plt.xlabel('x---->')
plt.ylabel('y---->')
plt.grid()


for n in n:
    t = np.arange(0, n, 1)
    y = f(t,n)[1]
    x = f(t,n)[0]
    lines1[0].set_xdata(t)
    lines1[0].set_ydata(x)# update plot data and redraw
    lines2[0].set_xdata(t)
    lines2[0].set_ydata(y)
    plt.draw()
    plt.pause(.2)

'''
