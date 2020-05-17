import sys
from Pyfhel import PyCtxt, PyPtxt, Pyfhel
import numpy as np
he = Pyfhel()
he.contextGen(p=5, m=8192)
he.keyGen()
p1 = he.encodeInt(1)
pminus1 = he.encodeInt(-1)
enc_minus = he.encryptInt(-1)
he.relinKeyGen(6,6)
p2 = he.encodeInt(2)

enc_zero = he.encryptInt(0)
enc_one = he.encryptInt(1)

def xlty(x_i, y_i):
    #print(he.decryptInt(x_i))
    #print(he.decryptInt(y_i))
    x = x_i
    y = y_i
    v1 = x_i + enc_minus
    v2 = v1 * y_i
    he.relinearize(v2)
    v = he.multiply_plain(v2, pminus1)
    he.relinearize(v)
    #print(he.noiseLevel(v))
    return v

def xeqy(x_i, y_i):
    x = x_i
    y = y_i
    v_mult = x * y
    v_mult_2 = v_mult + v_mult
    add_val = x + y
    v_xor = add_val - v_mult_2
    he.relinearize(v_xor)
    v_neg = he.multiply(v_xor, enc_minus)
    he.relinearize(v_neg)
    v_fin = he.add_plain(v_neg, p1)
    return v_fin


def SecComp():
    x = [0,0]
    e_x = []
    e_y = []
    y = [1,0]
    for i in range (0, len(x)):
        e_x.append(he.encryptInt(x[i]))
        e_y.append(he.encryptInt(y[i])) 
    l = len(x)
    z = [None]*l
    g = [None]*l
    #print(he.decryptInt(e_x[l-1]))
    #print(he.decryptInt(e_y[l-1]))
    
    g[l-1] = xeqy(e_x[l-1], e_y[l-1])
    he.relinearize(g[l-1])
    #print(he.noiseLevel(g[l-1]))
    for i in range (l-2, 0, -1):
        g[i] =  g[i+1] * xeqy(e_x[i],e_y[i])
        he.relinearize(g[i])
        #print(he.decryptInt(xeqy(e_x[i], e_y[i])))
        #print(he.noiseLevel(g[i]))
    #print(g)
    #for i in range(1,l):
        #print(he.decryptInt(g[i]))
    for i in range(0, l-1):
        z[i] = g[i+1] * xlty(e_x[i], e_y[i])
        he.relinearize(z[i])
        #print(he.noiseLevel(z[i]))
    z[l-1] = xlty(e_x[l-1], e_y[l-1])

    
    #print(he.decryptInt(z[l-1]))
    #print(he.decryptInt(xlty(e_x[l-1], e_y[l-1])))
    #print(he.decryptInt(e_x[l-1]))
    #print(he.decryptInt(e_y[l-1]))
    
    #for i in range(0, len(x)):
        #print(he.decryptInt(z[i]))
    #v = [None]*l
    #for i in range(0,l):
    #print(x)
    b = z[0]
    for i in range(1, len(z)):
        b = b + z[i] 
    return b
    #return 0

def SecComp1():
    x = [0,0]
    e_x = []
    e_y = []
    y = [0,1]
    for i in range (0, len(x)):
        e_x.append(he.encryptInt(x[i]))
        e_y.append(he.encryptInt(y[i])) 
    l = len(x)
    z = [None]*l
    g = [None]*l
    #print(he.decryptInt(e_x[l-1]))
    #print(he.decryptInt(e_y[l-1]))
    
    g[l-1] = xeqy(e_x[l-1], e_y[l-1])
    he.relinearize(g[l-1])
    #print(he.noiseLevel(g[l-1]))
    for i in range (l-2, 0, -1):
        g[i] =  g[i+1] * xeqy(e_x[i],e_y[i])
        he.relinearize(g[i])
        #print(he.decryptInt(xeqy(e_x[i], e_y[i])))
        #print(he.noiseLevel(g[i]))
    #print(g)
    #for i in range(1,l):
        #print(he.decryptInt(g[i]))
    for i in range(0, l-1):
        z[i] = g[i+1] * xlty(e_x[i], e_y[i])
        he.relinearize(z[i])
        #print(he.noiseLevel(z[i]))
    z[l-1] = xlty(e_x[l-1], e_y[l-1])

    
    #print(he.decryptInt(z[l-1]))
    #print(he.decryptInt(xlty(e_x[l-1], e_y[l-1])))
    #print(he.decryptInt(e_x[l-1]))
    #print(he.decryptInt(e_y[l-1]))
    
    #for i in range(0, len(x)):
        #print(he.decryptInt(z[i]))
    #v = [None]*l
    #for i in range(0,l):
    #print(x)
    b = z[0]
    for i in range(1, len(z)):
        b = b + z[i] 
    return b
    #return 0


def main():
      #for i in range (0,len(x)):
    #3print(e_x)
    value0 = SecComp()
    value1 = SecComp1()
    #b_0 = he.decryptInt(value)
    #b_1 = he.decryptInt(value1)
    l_00 = he.encryptInt(0)
    l_01 = he.encryptInt(0)
    l_10 = he.encryptInt(0)
    l_11 = he.encryptInt(1)
    l_20 = he.encryptInt(1)
    l_21 = he.encryptInt(1)
    oneminusb0 = enc_one - value0
    oneminusb1 = enc_one - value1
    v_0 = value0*l_00 + (oneminusb0*(value1*l_10 + oneminusb1*l_20))
    v_1 = value0*l_01 + (oneminusb0*(value1*l_11 + oneminusb1*l_21))
    dec_v0 = he.decryptInt(v_0)
    dec_v1 = he.decryptInt(v_1)
    print(dec_v0)
    print(dec_v1)

    label = dec_v0 + 2*(dec_v1)
    print("The label value is:", label)

if __name__ == "__main__":
    main()
