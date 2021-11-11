from vigilante import vigilar
from formato_tabla import crear_formateador
import informe_final
import csv

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def ticker(camion_file, log_file, fmt = 'txt'):
    rows = parsear_datos(vigilar(log_file))
    camion = informe_final.leer_camion(camion_file)
    rows = (row for row in rows if row['nombre'] in camion)
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre','Precio','Volumen'])
    for row in rows:
        formateador.fila([row[key] for key in row])

if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)