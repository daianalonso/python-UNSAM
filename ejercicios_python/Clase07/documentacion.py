#Ejercicio 7.10

def valor_absoluto(n):
    '''
    Calcula el valor absoluto de un número dado

    Pre: n es un número 
    Pos: Devuelve el valor absoluto del número n
    '''
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    '''
    Para un conjunto de números dado devuelve la suma entre los que son números pares

    Pre: l debe ser un iterable que contenga valores numéricos
    Pos: Devuelve la suma de los números pares de l, si no hubiera números pares devuelve 0
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
    #Invariante del ciclo: 
    # En la iteración i el parámetro res contiene el resultado de sumar los primeros i números pares de l 


def veces(a, b):
    '''
    Devuelve el valor de sumar el valor a, una cantidad b de veces

    Pre: b tiene que ser un número entero positivo
    Pos: Devuelve el resultado de sumar b veces el valor a 
    '''
    res = 0
    nb = b #Copio el valor b para poder usarlo como contador y no modificar su valor
    while nb != 0:
        res += a
        nb -= 1
    return res
    #Invariante del ciclo: 
    # En la iteración i la variable res contiene el resultado de sumar i veces el valor a 

def collatz(n):
    '''
    Calcula la cantidad de pasos necesarios de la sucesión de collatz para llegar a 1 empezando desde el número n 
    
    Pre: n es un número entero positivo
    Pos: Devuelve la cantidad de pasos necesarios de la sucesión de collatz para llegar a 1 empezando desde el número n
    '''
    res = 1

    while n!=1:
        #Si el número es par, se divide entre 2
        if n % 2 == 0:
            n = n//2
        else:  #Si el número es impar, se multiplica por 3 y se suma 1
            n = 3 * n + 1
        res += 1

    return res