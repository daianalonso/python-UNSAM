import random 
import numpy as np 
#Ejercicio 5.6
#Simular n mediciones de temperatura y devolverlos en una lista 
def medir_temp(n):
    mediciones = [random.normalvariate(0,0.2) for i in range(n)]
    temperaturas = np.array(mediciones)
    np.save( '../Data/temperaturas.npy',temperaturas)
    return mediciones

def resumen_temp(n):
    temperaturas = medir_temp(n)
    temperaturas.sort()
    maximo = max(temperaturas)
    minimo = min(temperaturas)
    #Si es impar veo el valor central de la lista ordenada
    medio = int(n/2)
    if len(temperaturas)%2 == 1:
        mediana = temperaturas[medio]
    else: #Sino promedio los valores centrales
        valor_medio1 = temperaturas[medio]
        valor_medio2 = temperaturas[medio-1]
        mediana = (valor_medio1 + valor_medio2)/2
    promedio = sum(temperaturas)/n
    return (maximo, minimo, promedio, mediana)


if __name__ == '__main__':
    #print(resumen_temp(999))
    b = np.load('../Data/temperaturas.npy')
    print(b)
