import random
import numpy as np

#Ejercicio 5.10
def crear_album(figus_total):
    return np.zeros(figus_total)

#Ejercicio 5.11
def album_incompleto(A):
    return (A == 0).sum() > 0

#Ejercicio 5.12
def comprar_figu(figus_total): 
    return random.randint(0,figus_total-1)

#Ejercicio 5.13
def cuantas_figus(figus_total):
    A = crear_album(figus_total)
    cant_figus = 0
    while album_incompleto(A):
        figu = comprar_figu(figus_total)
        A[figu] = 1
        cant_figus += 1
    return cant_figus
    
#Ejercicio 5.15
def experimento_figus(n_repeticiones, figus_total):
    L = [cuantas_figus(figus_total) for n in range(n_repeticiones)]
    return np.mean(L)

#Ejercicio 5.17
def comprar_paquete(figus_total, figus_paquete):
    return [comprar_figu(figus_total) for n in range(figus_paquete)]

#Ejercicio 5.18
def cuantos_paquetes(figus_total, figus_paquete):
    A = crear_album(figus_total)
    cant_paq = 0
    while album_incompleto(A):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete:
            A[figu] = 1
        cant_paq += 1
    return cant_paq

if __name__ == '__main__':
    print(experimento_figus(100, 670))
    L = [cuantos_paquetes(670,5) for n in range(100)]
    print(np.mean(L))
