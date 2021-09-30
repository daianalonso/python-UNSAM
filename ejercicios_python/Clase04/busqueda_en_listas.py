#Ejercicio 4.3
#Devuelve la posición de la última aparición de ese elemento en la lista 
# (o -1 si el elemento no pertenece a la lista)
def buscar_u_elemento(lista, elem):
    pos = -1       
    for i, e in enumerate(lista):  
        if e == elem:  
            pos = i      
    return pos

#Ejercicio 4.4
def maximo(lista):
    max = lista[0]
    for e in lista:
        if e > max:
            max = e
    return max

def minimo(lista):
    min = lista[0]
    for e in lista:
        if e < min:
            min = e
    return min 

if __name__ == '__main__':
    listado = [1,2,5,6,3,4,5]
    print(buscar_u_elemento(listado, 5))
    print(maximo([-5,-4]))
