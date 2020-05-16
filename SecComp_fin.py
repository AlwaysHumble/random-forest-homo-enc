import sys
from Pyfhel import PyCtxt, PyPtxt, Pyfhel
he = Pyfhel()
he.contextGen(p=2)
he.keyGen()
p1 = he.encodeInt(1)
pminus1 = he.encodeInt(-1)


def xlty(x_i, y_i):
    minusxi = he.multiply_plain(x_i, pminus1)
    add_one = he.add_plain(minusxi, p1)
    v = he.multiply(add_one, y_i)
    return v

def xeqy(x_i, y_i):
    add_val = he.add(x_i, y_i)
    v1 = he.add_plain(add_val, p1)
    return v1


def SecComp(x, y):
    l = x.length()
    g = []
    g[l-1] = xeqy(x[l-1], y[l-1])
    for i in range (l-2, 0):
        g[i] = he.multiply(g[i+1], xeqy(x[i],y[i])

    z = []
    for i in range (0,l-1):
        z[i] = he.multiply(xlty(x[i], y[i]), g[i+1])
        #z[i] = xlty(x[i], y[i]) & (g[i+1])


    z[l-1] = xlty(x[l-1], y[l-1])
    
    b = z[0]
    for i in range (1, l):
        b = he.add(b, z[i])

    return b


