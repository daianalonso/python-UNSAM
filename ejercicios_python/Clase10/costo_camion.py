import csv
import informe_final
import lote 

def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(filename)
    return camion.precio_total()

def f_principal(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion')
    print('Costo total:', costo_camion(parametros[1]))

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
