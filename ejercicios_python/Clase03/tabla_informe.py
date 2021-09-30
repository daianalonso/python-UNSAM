#Ejercicio 3.13
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
     camion = []
     with open(nombre_archivo, 'rt', encoding='utf8') as f:
         filas = csv.reader(f)
         encabezados = next(filas)
         for n_fila,fila in enumerate(filas, start=1):
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
            pass
            #print(f'Ups! No logro entender la linea {i+1}:{fila}')
    return dicc

def hacer_informe(cam, prec):
    nombres = []
    cajones = []
    precios_mercado = []
    lista_cambio = []
    for c in cam:
        nombres.append(c['nombre'])
        cajones.append(int(c['cajones']))
        precios_mercado.append(prec[c['nombre']])
        cambio = prec[c['nombre']] - float(c['precio'])
        lista_cambio.append(cambio)
    return list(zip(nombres,cajones,precios_mercado,lista_cambio))

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
guiones = '-'*8
print(f'{guiones:>10s} {guiones:>10s} {guiones:>10s} {guiones:>10s}')
for nombre, cajones, precio, cambio in informe:
    precio = '$' + str(precio)
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

#costo_camion = 0.0
#recaudacion = 0.0
#for c in camion:
#        costo_camion += float(c['cajones'])*float(c['precio'])
#        recaudacion += float(c['cajones']) * float(precios[c['nombre']])
#diferencia = recaudacion - costo_camion

#print(f'Costo del camion: {costo_camion:.2f}, Total recaudado: {recaudacion:.2f}, Balance: {diferencia:.2f}')
#if diferencia < 0:
#    print("Hubo pérdida")
#else: 
#    print("Hubo ganancia")