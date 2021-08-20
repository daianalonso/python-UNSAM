import csv
from pprint import pprint

#Ejercicio 2.15
# def leer_camion(nombre_archivo):
#     camion = []
#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             lote = (row[0], int(row[1]), float(row[2]))
#             camion.append(lote)
#     return camion

#Ejercicio 2.16
def leer_camion(nombre_archivo):
     camion = []
     with open(nombre_archivo, 'rt', encoding='utf8') as f:
         rows = csv.reader(f)
         headers = next(rows)
         for row in rows:
             cajon = {
                'nombre': row[0],
                'cajones': int(row[1]),
                'precio': float(row[2])
            }
             camion.append(cajon)
     return camion

#Ejercicio 2.17
def leer_precios(nombre_archivo):
    dicc = {}
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    for i,row in enumerate(rows):
        try:
            dicc[row[0]] = float(row[1])
        except IndexError:
            print(f'Ups! No logro entender la linea {i+1}:{row}')
    return dicc

#Ejercicio 2.18
camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
costo_camion = 0.0
recaudacion = 0.0
for c in camion:
        costo_camion += c['cajones']*c['precio']
        recaudacion += c['cajones'] * precios[c['nombre']]
diferencia = recaudacion - costo_camion

print(f'Costo del camion: {costo_camion:.2f}, Total recaudado: {recaudacion:.2f}, Balance: {diferencia:.2f}')
if diferencia < 0:
    print("Hubo pérdida")
else: 
    print("Hubo ganancia")