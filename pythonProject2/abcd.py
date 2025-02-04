import numpy as np

N = 100
M0 = 8
T = np.zeros(N)
for i in range(N):
    M = M0
    t = 0
    while M > 0:
        r = np.random.random()
        M = M + 1 if r > 0.5 else M - 1
        t = t + 1
    T[i] = t

mean = np.mean(T)
print('mean=', mean)

std = np.std(T)
print('std=', std)
