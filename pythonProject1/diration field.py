import math

class Array:
    def __init__(self):
        self.z = [0.0]*6

class Array1:
    def __init__(self):
        self.x = [0.0]*100
        self.y = [0.0]*100

class Array2:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

def u(x,y):
    g = Array()

    g.z[0] = x*x*x - 3*x*y*y - 1 # u(x,y)
    g.z[1] = 3*x*x*y - y*y*y   # v(x,y)
    g.z[2] = 3*x*x - 3*y*y   # ux(x,y)
    g.z[3] = -6*x*y   # uy(x,y)
    g.z[4] = 6*x*y   # vx(x,y)
    g.z[5] = 3*x*x - 3*y*y  # vy(x,y)

    return g

def fun(x0, y0):
    # print("give the guess values")
    # x0 = float(input())
    # y0 = float(input())
    a = Array()
    b = Array2()
    while True:
        a = u(x0, y0)
        d = a.z[2]*a.z[5] - a.z[3]*a.z[4] # determinant
        delx = -(a.z[5]*a.z[0] - a.z[3]*a.z[1])/d
        dely = -(a.z[2]*a.z[1] - a.z[4]*a.z[0])/d
        x0 = x0 + delx
        y0 = y0 + dely
        b.x = x0
        b.y = y0
        if abs(a.z[0]) + abs(a.z[1]) <= 0.0001:
            break

    return b

def main():
    d = Array1()
    y0 = 0.0
    x0 = 0.0
    i = 0

    for x0 in [round(-2+0.1*i,1) for i in range(41)]:
        for y0 in [round(-2+0.1*j,1) for j in range(41)]:
            b = fun(x0, y0)
            if b.x == 1 and b.y < 0.00001:
                d.x[i] = x0
                d.y[i] = y0
                print(f"   {x0}, {y0}")
                i = i + 1

if __name__ == "__main__":
    main()