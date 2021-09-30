#Ejercicio 6.13
def busqueda_lineal_lordenada(lista,e):
    pos = -1     
    for i, elem in enumerate(lista):  
        if elem > e:
            return -1 
        if e == elem:  
            pos = i      
    return pos