#%%Ejercicio 12.4
import random
import numpy as np
import matplotlib.pyplot as plt

def generar_lista(N):
    return [random.randint(1, 1000) for i in range(N)]

def ord_burbujeo(lista):
    '''
    Ordena la lista utilizando ordenamiento por burbujeo (intercambios)
    Cuenta la cantidad de comparaciones.'''
    n = len(lista)
    count = 0
    #Por cada elemento de la lista
    for i in range(n):
        #Lo voy corriendo hasta la posición que le corresponda
        #Invariante: los últimos i elementos ya están ordenados
        for j in range(0, n-i-1):
            count +=1
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return count

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    count = 0
    for i in range(len(lista) - 1):
        count += 1
        if lista[i + 1] < lista[i]:
            count += reubicar(lista, i + 1)
    return count

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    count = 0
    v = lista[p]
    j = p
    while j > 0 and v < lista[j - 1]:
        count += 1
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v
    return count

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
        Cuenta la cantidad de comparaciones. 
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    count = 0
    n = len(lista) - 1

    while n > 0:
        p, c = buscar_max(lista, 0, n)
        count += c
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    
    return count

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables. También la cantidad de comparaciones que realizó. 
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    count = 0
    for i in range(a + 1, b + 1):
        count += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, count

#%%Ejercicio 12.16
def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    contador, i, j = 0, 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        contador += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, contador

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    cant_comp = 0

    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, c_izq = merge_sort(lista[:medio])
        der, c_der = merge_sort(lista[medio:])
        lista_nueva, c_merge = merge(izq, der)

        cant_comp = c_izq + c_der + c_merge
    
    return lista_nueva, cant_comp

def experimento(N, k):
    '''Repite k veces generar una lista de largo N,
     ordena la lista con los tres métodos y promedia la cantidad de operaciones realizadas'''
    comp_selection = 0
    comp_burbujeo = 0
    comp_insertion = 0
    comp_merge = 0
    for K in range(k):
        lista = generar_lista(N)
        comp_selection += ord_seleccion(lista.copy())
        comp_burbujeo += ord_burbujeo(lista.copy())
        comp_insertion += ord_insercion(lista.copy())
        comp_merge += merge_sort(lista.copy())[1]
    #Promedio los valores
    comp_burbujeo = comp_burbujeo/k
    comp_selection = comp_selection/k
    comp_insertion = comp_insertion/k
    comp_merge = comp_merge/k
    return (comp_burbujeo, comp_insertion, comp_selection, comp_merge)

#%% Ejercicio 12.15
def experimento_vectores(Nmax):
    '''
    Comparación visual de  la cantidad de comparaciones que realiza cada algoritmo
    Merge sort a medida que incrementa el tamaño de la lista, realiza menos 
    comparaciones que los demás métodos. Selection sort y Bubble sort se comportan igual.
    '''
    comparaciones_seleccion = np.zeros(Nmax)
    comparaciones_insercion = np.zeros(Nmax)
    comparaciones_burbujeo = np.zeros(Nmax)
    comparaciones_merge = np.zeros(Nmax)

    for N in range(1, Nmax):
        res_burb, res_ins, res_sel, res_merge = experimento(N, 100)
        comparaciones_burbujeo[N] = res_burb
        comparaciones_insercion[N] = res_ins
        comparaciones_seleccion[N] = res_sel
        comparaciones_merge[N] = res_merge
    
    x = np.linspace(1, Nmax, Nmax)
    plt.plot(x, comparaciones_seleccion, color='red', label='Selection sort')
    plt.plot(x, comparaciones_burbujeo, color='black', label='Bubble sort', linestyle='--')
    plt.plot(x, comparaciones_insercion, color='blue', label='Insertion sort')
    plt.plot(x, comparaciones_merge, color='green', label='Merge sort')
    
    plt.xlabel("Tamaño de lista")
    plt.ylabel("Número de comparaciones")
    plt.title("Complejidad algoritmos de ordenamiento")
    
    plt.legend()


#%%
if __name__ == "__main__":
    lista = [3, 2, -1, 5, 0, 2]
    print(ord_insercion(lista))
    lista = [5, 4, 3, 2, 1]
    print(ord_burbujeo(lista))
    print(experimento(10, 100))
    experimento_vectores(100)
# %%
