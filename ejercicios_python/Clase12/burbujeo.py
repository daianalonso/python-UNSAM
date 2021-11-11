def ord_burbujeo(lista):
    '''
    Ordena la lista utilizando ordenamiento por burbujeo (intercambios)
    Complejidad: O(n^2). Ya que realiza O(n^2) comparaciones  
    '''
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
    return lista

def ord_burbujeo_recursivo(lista, n):
    ''' 
    Función de ordenamiento por burbujeo
    '''
    #Recorro la lista llevando el elemento máximo hacia el final
    for i in range(n - 1):
        if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
            
    #Si no llegué al caso base (cuando me queda el último por ordenar)
    if n-1 > 1:
        ord_burbujeo_recursivo(lista, n-1)

if __name__ == '__main__':
    lista = [0, 9, 3, 8, 5, 3, 2, 4]
    print(ord_burbujeo(lista))
    lista = [1,4,8,2,3,9,4,7]
    ord_burbujeo_recursivo(lista, len(lista))
    print(lista)