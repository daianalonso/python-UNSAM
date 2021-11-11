import csv
from fileparse import parse_csv
import lote
import formato_tabla

#%%
def leer_camion(nombre_archivo):
    with open(nombre_archivo) as files:
        camion_dicts = parse_csv(files, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion

#%%
def leer_precios(nombre_archivo):
    with open(nombre_archivo) as files:
        lista_precios =  parse_csv(files, types = [str, float], has_headers = False)
    return dict(lista_precios)
#%%
def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        cambio = precios[lote.nombre] - lote.precio
        lista.append((lote.nombre,lote.cajones,lote.precio,cambio))
    return lista

#%% Ejercicio 9.5
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

#%% Ejercicio 9.7
def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)

#%% Ejercicio 7.4 
def f_principal(parametros):
    if len(parametros) != 4:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')
    informe_camion(parametros[1],parametros[2], parametros[3])

#%%
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)