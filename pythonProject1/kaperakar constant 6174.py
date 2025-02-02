import numpy as np
import math


def f1(m, num):
    iteration_num = 0
    bignum = 0
    smallnum = 0
    diff1 = 0
    diff2 = 0

    while num != diff2:
        n = []
        diff2 = diff1
        diff1 = num

        for k in range(m):
            n[k] = num / 10 ** (m - (k + 1))
            r = num % 10 ** (m - (k + 1))
            num = r

        for i in range(m - 1):
            for j in range(i + 1, m):
                if n[i] > n[j]:
                    n[i], n[j] = n[j], n[i]

        for k in range(m):
            bignum += n[k] * 10 ** k
            smallnum += n[k] * 10 ** (m - (k + 1))

        diff = bignum - smallnum
        num = diff

        print("newnum =", diff)
        iteration_num += 1
    print("Number of iterations =", iteration_num)
    return (iteration_num)


m = input('give no of digit')
num1 = input('give the number')
print(f1(m, num1))
