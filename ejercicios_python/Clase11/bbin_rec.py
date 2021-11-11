#%%Ejercicio 11.11
def bbinaria_rec(lista, e):
    '''Implementa la busqueda binaria de forma recursiva'''
    if len(lista) == 0:
        res = False
    elif len(lista) == 1: #Si la lista quedó con un elemento, me fijo si es "e"
        res = lista[0] == e
    else:
        #Divido la lista en dos y llamo recursivamente para cada parte
        medio = len(lista)//2
        res = bbinaria_rec(lista[:medio], e) or bbinaria_rec(lista[medio:], e)
    return res