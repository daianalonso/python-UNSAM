#%%Ejercicio 11.14
import numpy as np 
import matplotlib.pyplot as plt 

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(superficie, alquiler)

g = plt.scatter(x = superficie, y = alquiler)
plt.title('y ajuste lineal')
plt.plot(superficie, superficie*a+b, c = 'green')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
#%%