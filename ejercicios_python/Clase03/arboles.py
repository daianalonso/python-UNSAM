#Ejercicio 3.18
import csv
from collections import Counter
from os import sep

def leer_parque(nombre_archivo, parque):
    arboles = []
    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezados = next(filas)
    for fila in filas:
        if(fila[10] == parque):
            registro = dict(zip(encabezados,fila))
            arboles.append(registro)
    return arboles

#Ejercicio 3.19
#Toma una lista de arboles y devuelve el conjunto de especies
def especies(lista_arboles):
    arboles = []
    for arbol in lista_arboles:
        arboles.append(arbol['nombre_com'])
    return set(arboles)

#Ejercicio 3.20
#Devuelve un diccionario en el que las especies son las claves y tienen como valores asociados la cantidad
#  de ejemplares en esa especie en la lista dada.
def contar_ejemplares(lista_arboles):
    contador = Counter()
    for arbol in lista_arboles:
        nombre_arbol = arbol['nombre_com'];
        contador[nombre_arbol] += 1
    return contador

arboles_gralPaz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
arboles_losAndes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
arboles_centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

#print('General Paz',contar_ejemplares(arboles_gralPaz).most_common(5))
#print('Los Andes',contar_ejemplares(arboles_losAndes).most_common(5))
#print('Centenario',contar_ejemplares(arboles_centenario).most_common(5))

#Ejercicio 3.21
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if (arbol['nombre_com'] == especie):
            alturas.append(float(arbol['altura_tot']))
    return alturas    

headers = ('Medida', 'General Paz', 'Los Andes', 'Centenario')
#print(f'{headers[0]} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
alturas_gralpaz = obtener_alturas(arboles_gralPaz, 'Jacarandá')
max_generalpaz = max(alturas_gralpaz)
prom_generalpaz = sum(alturas_gralpaz)/len(alturas_gralpaz)

alturas_centenario = obtener_alturas(arboles_centenario, 'Jacarandá')
max_centenario = max(alturas_centenario)
prom_centenario = sum(alturas_centenario)/len(alturas_centenario)

alturas_losandes = obtener_alturas(arboles_losAndes, 'Jacarandá')
max_losandes = max(alturas_losandes)
prom_losandes = sum(alturas_losandes)/len(alturas_losandes)
#print(f'max {max_generalpaz:>10.2f} {max_losandes:>10.2f} {max_centenario:>10.2f}')
#print(f'prom {prom_generalpaz:>9.2f} {prom_losandes:>10.2f} {prom_centenario:>10.2f}')

#Ejercicio 3.22
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if (arbol['nombre_com'] == especie):
           inclinaciones.append(int(arbol['inclinacio']))
    return inclinaciones

#Ejercicio 3.23
def especimen_mas_inclinado(lista_arboles):
    mas_inclinado = ['especie', 0]
    for arbol in lista_arboles:
        inclinacion_maxima = max(obtener_inclinaciones(lista_arboles, arbol['nombre_com']))
        if (mas_inclinado[1] < inclinacion_maxima):
            mas_inclinado[0] = arbol['nombre_com']
            mas_inclinado[1] = inclinacion_maxima
    return mas_inclinado

#print('General Paz', especimen_mas_inclinado(arboles_gralPaz)) 
#print('Los Andes', especimen_mas_inclinado(arboles_losAndes))
#print('Parque Centenario', especimen_mas_inclinado(arboles_centenario))

#Ejercicio 3.24
def especie_promedio_mas_inclinada(lista_arboles):
    mas_inclinada = ['especie', 0]
    for arbol in lista_arboles:
        inclinaciones = obtener_inclinaciones(lista_arboles, arbol['nombre_com'])
        inclinacion_promedio = sum(inclinaciones)/len(inclinaciones)
        if (mas_inclinada[1] < inclinacion_promedio):
            mas_inclinada[0] = arbol['nombre_com']
            mas_inclinada[1] = inclinacion_promedio
    return mas_inclinada

print('General Paz', especie_promedio_mas_inclinada(arboles_gralPaz)) 
print('Los Andes', especie_promedio_mas_inclinada(arboles_losAndes))
print('Parque Centenario', especie_promedio_mas_inclinada(arboles_centenario))