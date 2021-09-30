import csv
from fileparse import parse_csv
#%%
def leer_camion(nombre_archivo):
    return parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

#%%
def leer_precios(nombre_archivo):
    return parse_csv(nombre_archivo, types = [str, float], has_headers = False)
#%%
def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = dict(precios)[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista

#%% Ejercicio 6.4
def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)

#%% Ejercicio 6.5
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    informe = hacer_informe(leer_camion(nombre_archivo_camion), leer_precios(nombre_archivo_precios))
    imprimir_informe(informe)

#%%
if __name__ == '__main__':
    informe_camion('../Data/camion.csv','../Data/precios.csv')
# %%
