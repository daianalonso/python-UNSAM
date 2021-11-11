#%%Ejercicio 11.9
def pascal(n, k):
    '''Función recursiva que devuelve el valor del triangulo de pascal de la fila n columna k'''
    if n < 0 or k < 0: #Consulta inválida
        return 0
    if n == k or k == 0: #Estamos en los bordes del triangulo o en la punta
        return 1
    return pascal(n-1, k-1) + pascal(n-1, k)
    
