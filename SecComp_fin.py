import sys

def xlty(x_i, y_i):
    return (1-x_i)*y_i

def xeqy(x_i, y_i):
    return 1 + x_i^y_i


def SecComp(x, y):
    l = x.length()
    g = []
    g[l-1] = xeqy(x[l-1], y[l-1])
    for i in range (l-2, 0):
        g[i] = g[i+1] & xeqy(x[i], y[i])

    z = []
    for i in range (0,l-1):
        z[i] = xlty(x[i], y[i]) & (g[i+1])


    z[l-1] = xlty(x[l-1], y[l-1])
    
    b = z[0]
    for i in range (1, l):
        b = b or z[i]

    return b
