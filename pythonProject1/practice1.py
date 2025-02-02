#Data set of Frank Hertz exp 
# above one is first one and in this code i have 2-5 no set

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
# Data Sets
data_set_2_voltage = [1.0, 3.0, 5.0, 7.0, 8.1, 9.1, 10, 11, 12, 13.1, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,51, 53, 54, 55, 56, 57, 58, 60, 62, 64, 66, 68, 69, 70, 71, 73]
data_set_2_current = [0.02, 0.02, 0.02, 0.02, 0.12, 1.05, 2.31, 3.52, 4.37, 4.91, 5.39, 5.78, 6.02, 6.03, 5.68, 5.04, 4.11, 3.29, 3.33, 4.37, 5.58, 6.86, 7.74, 8.28, 8.37, 7.88, 6.77, 5.05, 3.41, 2.34, 3.25, 5.38, 7.68, 9.41, 10.59, 10.96, 10.73, 9.79, 7.95, 5.77, 3.58, 2.63, 4.18, 7.02, 9.64, 12.01, 13.29,15.21,
           13.58, 11.44, 8.55, 5.79, 4.63, 6.04, 11.99, 16.73, 17.66, 15.02, 9.58, 7.92, 8.18, 10.04, 15.50]

data_set_3_voltage = [1.0, 3.0, 5.0, 7.0, 8.1, 9.1, 10, 11, 12, 21, 21.5, 22, 22.5, 23, 32, 32.5, 33, 33.5, 44, 44.5, 45, 45.5, 46, 56, 56.5, 57, 57.5, 58, 68, 68.5, 69, 69.5, 70, 70.5]
data_set_3_current = [0.02, 0.02, 0.02, 0.02, 0.14, 1.35, 2.65, 3.85, 4.84, 3.79, 3.73, 3.97, 4.45, 5.14, 3.80, 3.13, 2.80, 3.12, 3.92, 3.12, 3.03, 3.64, 4.71, 5.61, 4.78, 4.55, 5.03, 5.96, 9.43, 8.11, 7.64, 7.66, 8.01, 8.82 ]

data_set_4_voltage = [20, 20.5, 21, 21.5, 22, 32, 32.5, 33, 33.5, 34, 34.5, 44, 44.5, 45, 45.5, 46, 56, 56.5, 57, 57.5, 58, 58.5, 68, 68.5, 69, 69.5, 70]
data_set_4_current = [4.28, 3.23, 3.21, 3.30, 3.62, 3.56, 2.94, 2.70, 3.03, 3.73, 4.92, 3.82, 3.02, 2.97, 3.67, 4.68, 5.50, 4.72, 4.55, 5.05, 6.04, 7.18, 9.05, 8.07, 7.62, 7.56, 7.93]

data_set_5_voltage = [20, 20.5, 21, 21.5, 22, 22.5, 32, 32.5, 33, 33.5, 34, 44, 44.5, 45, 45.5, 46, 56, 56.5, 57, 57.5, 58, 68, 68.5, 69, 69.5, 70, 70.5]
data_set_5_current = [4.46, 3.96, 3.67, 3.66, 3.95, 4.42, 3.81, 3.05, 2.77, 3.07, 3.81, 3.76, 3.06, 2.96, 3.60, 4.60, 5.40, 4.74, 4.49, 5.02, 5.87, 9.13, 7.98, 7.52, 7.44, 7.88, 8.61]



x_new = np.linspace(20, 70, 500)
bspline = interpolate.make_interp_spline(data_set_2_voltage, data_set_2_current)
y_new = bspline(x_new)

# Create Subplots
plt.figure(figsize=(12, 8))

# Subplot 1
plt.subplot(2, 2, 1)
plt.plot(data_set_2_voltage, data_set_2_current)
plt.title('Data Set 2')
plt.xlabel('Voltage')
plt.ylabel('Current')
plt.plot(x_new, y_new,linestyle='--', color='k', label='smooth curve')


# Subplot 2
plt.subplot(2, 2, 2)
plt.plot(data_set_3_voltage, data_set_3_current)
plt.title('Data Set 3')
plt.xlabel('Voltage')
plt.ylabel('Current')

# Subplot 3
plt.subplot(2, 2, 3)
plt.plot(data_set_4_voltage, data_set_4_current)
plt.title('Data Set 4')
plt.xlabel('Voltage')
plt.ylabel('Current')

# Subplot 4
plt.subplot(2, 2, 4)
plt.plot(data_set_5_voltage, data_set_5_current)
plt.title('Data Set 5')
plt.xlabel('Voltage')
plt.ylabel('Current')


# Adjust layout
plt.tight_layout()

# Show the plots
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