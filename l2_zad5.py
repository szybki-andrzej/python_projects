import numpy as np
import matplotlib.pyplot as plt

#metoda lagrange'a

xs = np.linspace(0, np.pi/2, 100)

xx = [0, np.pi/4, np.pi/2]

def lagr(xx,x):
    prev = 0
    for i in range(len(xx)):
        prev = prev + np.cos(xx[i])*li(xx,i,x)
    return prev

def li(xx,i,x):
    prev = 1
    for j in range(len(xx)):
        if j != i:
            prev = prev*((x-xx[j])/(xx[i]-xx[j]))
    return prev

plt.plot(xs, np.cos(xs), label = "cos(x)")
plt.plot(xs, lagr(xx,xs), color = "red",label = "p_2(x)")
plt.legend()
plt.show()

def err(x):
    return abs((x*(x-np.pi/2)*(x-np.pi/4))/6)

max_err = max([err(x) for x in xs])
print(max_err)

max_err2 = max([np.abs(lagr(xx,x)-np.cos(x)) for x in xs])
print(max_err2)
print(max_err2/max_err)

plt.plot(xs, np.abs(lagr(xx,xs)-np.cos(xs)), label = "g(x)")
plt.plot(xs, err(xs), color = "red", label = "wartość teoretyczna")
plt.legend()
plt.show()


#metoda newtona

c0 = np.cos(xx[0])
c1 = ((np.cos(xx[1])-np.cos(xx[0]))/(xx[1]-xx[0]))
c2 = (((np.cos(xx[2])-np.cos(xx[1]))/(xx[2]-xx[1])) - ((np.cos(xx[1])-np.cos(xx[0])))/(xx[1]-xx[0]))/(xx[2]-xx[0])

cc = [c0, c1, c2]

def gj(xx,j,x):
    prev = 1
    for i in range(j):
        prev = prev*(x-xx[i])
    return prev


def newt(xx,x):
    prev = 0
    for i in range(len(xx)):
        prev = prev + cc[i]*gj(xx,i,x)
    return prev

plt.plot(xs, np.cos(xs), label = "cos(x)")
plt.plot(xs, newt(xx,xs), color = "red", label = "p_2(x)")
plt.legend()
plt.show()

plt.plot(xs, np.abs(newt(xx,xs)-np.cos(xs)), label = "p_2(x)")
plt.plot(xs, err(xs), color = "red", label = "wartość teoretyczna")
plt.legend()
plt.show()

