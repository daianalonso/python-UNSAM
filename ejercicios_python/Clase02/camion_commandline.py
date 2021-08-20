#Ejercicio 2.10
import csv
import sys
def costo_camion(nombre_archivo):
    costo_pagado = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for line in rows:
        try:
            cantidad = float(line[-1])
            precio = float(line[-2])
            costo_pagado += cantidad * precio
        except ValueError:
            print('Warning: faltan datos en una celda')
    return costo_pagado

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)