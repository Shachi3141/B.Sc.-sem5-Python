#Date 25 sep,2023 (Shachidev Mahato)
#Frank-Hertz exp data
#Find voltage diff b/t two consicutive min
#Here i use loc_diff function to get avg volt diff,it work--->
# 1)find loc minima
# 2)corrosponding voltages
# 3)find diff than avg


import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# V_G1K=1.51 v
# V_G2A=7.55 v

# Data
voltage = [1, 3, 5, 7, 8, 9, 11, 13, 15, 17, 19, 20, 21, 22, 23, 25, 27, 29, 30, 31, 32, 33, 34, 35, 37, 39, 41, 42, 43,
           44, 45, 46, 47, 49, 51, 53, 54, 55, 56, 57, 58, 60, 62, 64, 66, 68, 69, 70, 71, 73, 75, 77, 79, 81, 83, 85]
current = [0.02, 0.02, 0.02, 0.02, 0.20, 1.42, 4.05, 5.65, 6.60, 6.87, 5.73, 4.75, 3.74, 3.87, 5.02, 7.77, 9.45, 8.99,
           7.73, 5.77, 3.87, 2.73, 3.72, 6.23, 10.77, 12.45, 10.96, 9.03, 6.51, 3.91, 2.97, 4.70, 7.64, 13.27, 15.21,
           13.58, 11.44, 8.55, 5.79, 4.63, 6.04, 11.99, 16.73, 17.66, 15.02, 9.58, 7.92, 8.18, 10.04, 15.50, 19.45,
           20.40, 17.40, 12.93, 12.66, 16.42]

print(len(voltage))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(voltage, current, marker='o', linestyle='-', color='b', label='Voltage vs. Current')



#Here i use "interpolate.make_interp_spline" to make the curve smooth
# new variable: x_new, bspline, y_new
x_new = np.linspace(8, 85, 500)
bspline = interpolate.make_interp_spline(voltage, current)
y_new = bspline(x_new)

# Plot the new data points
plt.plot(x_new, y_new,linestyle='--', color='k', label='smooth curve')
plt.xlabel('Voltage')
plt.ylabel('Current in 10^-8 Ampere')
plt.title('Current vs. Voltage')
plt.legend()
plt.grid(True)
plt.show()

def loc_min(voltage,current):
    min_voltage=[]
    l = len(voltage)
    j = 0
    print('min current are:')
    for i in range(0, l - 2, 1):
        m1 = current[i + 1] - current[i]
        m2 = current[i + 2] - current[i + 1]
        if m1 < 0 and m2 > 0 :
         print(current[i + 1])
         min_voltage.append(voltage[i + 1])
         j = j + 1

    print('corrosponding voltages are ',min_voltage)
    val=0
    print('voltage difference between two consicutive min are:')
    for k in range(len(min_voltage)-1):
        diffr=min_voltage[k+1]-min_voltage[k]
        print(diffr)
        val=val+diffr
    return(val/(len(min_voltage)-1))
x=loc_min(x_new, y_new)
print('Avg voltage diff is')
print(x)
