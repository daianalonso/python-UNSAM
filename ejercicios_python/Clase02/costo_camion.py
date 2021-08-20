import csv
#Ejercicio 2.2
# costo_pagado = 0
#with open('../Data/camion.csv', 'rt') as f:
#    headers = next(f)
#    for line in f:
#        data = line.split(',')
#        cantidad = float(data[-1])
#        precio = float(data[-2])
#        costo_pagado += cantidad * precio
#print(f'Costo pagado {costo_pagado}')

#Ejercicio 2.6
#def costo_camion(nombre_archivo):
#    costo_pagado = 0
#    with open(nombre_archivo, 'rt') as f:
#        headers = next(f)
#        for line in f:
#            data = line.split(',')
#            cantidad = float(data[-1])
#            precio = float(data[-2])
#            costo_pagado += cantidad * precio
#    return costo_pagado

#costo = costo_camion('../Data/camion.csv')
#print('Costo total:', costo)

#Ejercicio 2.8
# def costo_camion(nombre_archivo):
#     costo_pagado = 0
#     with open(nombre_archivo, 'rt') as f:
#         headers = next(f)
#         for line in f:
#             data = line.split(',')
#             try:
#                 cantidad = float(data[-1])
#                 precio = float(data[-2])
#                 costo_pagado += cantidad * precio
#             except ValueError:
#                 print('Warning: faltan datos en una celda')
#     return costo_pagado

# costo = costo_camion('../Data/missing.csv')
# print('Costo total:', costo)

#Ejercicio 2.9
def costo_camion(nombre_archivo):
    total = 0.0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        try:
            cantidad = int(row[1])
            precio = float(row[2])
            total += cantidad * precio
        except ValueError:
            print('Warning: faltan datos en una celda')
    return total

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)