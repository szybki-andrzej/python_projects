import numpy as np
import matplotlib.pyplot as plt

x0 = 0.1
x1 = 0.2
k = 10
a = 0
b = 1

lista2 = []

def func(x):
    return (1/x)-2

def func_2(x):
    return 2*np.exp(-1)*x + 1 - 3*np.exp(-x)

def met_bis(a, b, func):
    x1 = (a+b)/2
    lista2.append(x1)
    while not (-(10**(-6))< func_2(x1) < 10**(-6)):

        x1 = (a+b)/2
        if func(a)*func(x1)<0:
            b = x1
        if func(x1)*func(b)<0:
            a = x1
        lista2.append(x1)
    return (a+b)/2

met_bis(a,b,func_2)

def met_siecz(x0,x1,k,func):
    xn1 = x1
    xn0 = x0
    for i in range(k):
        b = (func(xn1)*xn0 - func(xn0)*xn1)/(func(xn1)-func(xn0))
        xn0 = xn1
        xn1 = b
    return xn1

lista = []
t = np.linspace(1,k,k)
for i in range(k):
    lista.append(met_siecz(x0,x1,i,func))

t_bis = np.linspace(1,len(lista2), len(lista2))

plt.scatter(t, lista)
plt.show()
plt.scatter(t_bis, lista2)
plt.show()

xn_list = []
yn_list = []
for i in lista[1:]:
    yn_list.append(np.log(abs(i-0.5)))

for i in lista[:len(lista)-1]:
    xn_list.append(np.log(abs(i-0.5)))

a = np.polyfit(xn_list, yn_list, 1)[0]
b = np.polyfit(xn_list, yn_list, 1)[1]
print(np.polyfit(xn_list, yn_list, 1))

xx = np.linspace(min(xn_list), max(xn_list))
plt.scatter(xn_list, yn_list)
plt.show()

print(met_siecz(x0,x1,k,func))



