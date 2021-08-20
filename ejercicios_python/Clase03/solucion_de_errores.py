#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El primer y último caso arrojaban resultados erróneos, eso sucedía porque en el if devolvía un resultado
#al hacer la comparación con el primer caracter y cortaba la iteración del ciclo. También no indentificaba las 'A'.
#Se soluciona devolviendo verdadero cuando encontró una 'a' o 'A' en la palabra, o falso solo cuando termino la iteración del ciclo.
#A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in 'aA':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: Los errores se encuentran en:
#La declaracion de la función, el bucle y en la condición if, falta el símbolo ':' para indicar donde comienza
#La condición del if usa '=' en la expresión de comparación por igual en lugar de '=='
#Al final para devolver la expresión booleana 'False' usa 'Falso'
#Nuevamente el caso de prueba con 'A' devolverá False porque no considera mayúsculas en la comparación de caracteres
#A continuación el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in 'aA':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: Al querer contabilizar la cantidad de caracteres en la expresión, al tener en el último caso de prueba
#un input entero (int), este no tiene como atributo la función 'len' para obtener su longitud.
#Una solución sería convertir a cadena de caracteres el input en todos los casos
#A continuación el código corregido:
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
#%%
#Ejercicio 3.4. Función suma(a,b)
#Comentarios: En la función suma la variable c dentro de ella se queda en el scope de la función y se destruye luego
# de llamarla. La solución es que la función devuelva el valor de c
#Código corregido:
def suma(a,b):
    c = a + b
    return c
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
#%%
#Ejercicio 3.5. Pisando memoria
#En la función al diccionario registro se lo agrega a la lista camión, por lo tanto se asigna una copia que apunta
# a registro, pero como a este se lo redefine constantemente en el ciclo for, por consecuente el diccionario
#registro tendrá como valor el último asignaado. Esto hace que tengamos múltiples copias del último valor que se 
#leyó del camión.
#A continuación una posible corrección del código, creando un nuevo registro en cada iteración:
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)