import csv
from informe_funciones import leer_camion
def costo_camion(nombre_archivo):
    costo_total = 0.0
    camion = leer_camion(nombre_archivo)
    for fruta in camion:
        ncajones = fruta['cajones']
        precio = fruta['precio']
        costo_total += ncajones * precio
    return costo_total

if __name__ == '__main__':
    costo = costo_camion('../Data/fecha_camion.csv')
    print('Costo total:', costo)