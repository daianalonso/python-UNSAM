import csv
from informe_final import leer_camion
import lote 

def costo_camion(nombre_archivo):
    costo_total = 0.0
    camion = leer_camion(nombre_archivo)
    for fruta in camion:
        costo_total += fruta.costo()
    return costo_total

def f_principal(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion')
    print('Costo total:', costo_camion(parametros[1]))

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
