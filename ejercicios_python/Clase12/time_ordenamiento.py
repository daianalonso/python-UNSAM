#%%
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import timeit as tt

def generar_lista(N):
    return [random.randint(1, 1000) for i in range(N)]

def generar_listas(Nmax):
    listas = []
    for N in range(1, Nmax+1):
        listas.append(generar_lista(N))
    return listas

def ord_burbujeo(lista):
    '''
    Ordena la lista utilizando ordenamiento por burbujeo (intercambios)
    Cuenta la cantidad de comparaciones.'''
    n = len(lista)
    #Por cada elemento de la lista
    for i in range(n):
        #Lo voy corriendo hasta la posición que le corresponda
        #Invariante: los últimos i elementos ya están ordenados
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    j = p
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
        Cuenta la cantidad de comparaciones. 
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    n = len(lista) - 1
    while n > 0:
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables. También la cantidad de comparaciones que realizó. 
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    cant_comp = 0

    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def experimento_timeit(Nmax):
    ''' Comparación visual del tiempo de ejecución de los algoritmos.
    Selection sort y bubble sort tienen similar cantidad de comparaciones pero 
    podemos ver que bubble sort tarda más tiempo de ejecución.
    '''
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge = []

    global lista

    listas = generar_listas(Nmax)

    for lista in listas:
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = 100, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = 100, globals = globals())
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = 100, globals = globals())
        tiempo_merge = tt.timeit('merge_sort(lista.copy())', number = 100, globals = globals())
        # Guardo los resultados para cada método
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_merge.append(tiempo_merge)

    # Convierto los tiempos a array para plotear
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_merge = np.array(tiempos_merge)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    
    x = np.linspace(1, Nmax, Nmax)
    plt.plot(x, tiempos_seleccion, color='red', label='Selection sort')
    plt.plot(x, tiempos_burbujeo, color='black', label='Bubble sort')
    plt.plot(x, tiempos_insercion, color='blue', label='Insertion sort')
    plt.plot(x, tiempos_merge, color='green', label='Merge sort')
    
    plt.xlabel("Tamaño de lista")
    plt.ylabel("Tiempo de ejecución")
    plt.title("Complejidad algoritmos de ordenamiento")
    
    plt.legend()

if __name__ == "__main__":
    experimento_timeit(100)