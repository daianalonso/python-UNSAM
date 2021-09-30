#Ejercicio 3.9 Agregar zip 
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
     camion = []
     with open(nombre_archivo, 'rt', encoding='utf8') as f:
         filas = csv.reader(f)
         encabezados = next(filas)
         for fila in filas:
             record = dict(zip(encabezados, fila))
             camion.append(record)
     return camion

def leer_precios(nombre_archivo):
    dicc = {}
    f = open(nombre_archivo, 'r')
    filas = csv.reader(f)
    for i,fila in enumerate(filas, start=1):
        try:
            dicc[fila[0]] = float(fila[1])
        except IndexError:
            print(f'Ups! No logro entender la linea {i+1}:{fila}')
    return dicc

camion = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')
costo_camion = 0.0
recaudacion = 0.0
for c in camion:
        costo_camion += float(c['cajones'])*float(c['precio'])
        recaudacion += float(c['cajones']) * float(precios[c['nombre']])
diferencia = recaudacion - costo_camion

print(f'Costo del camion: {costo_camion:.2f}, Total recaudado: {recaudacion:.2f}, Balance: {diferencia:.2f}')
if diferencia < 0:
    print("Hubo pérdida")
else: 
    print("Hubo ganancia")