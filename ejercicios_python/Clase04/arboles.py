#Ejercicio 4.15
import csv

def leer_arboles(nombre_archivo):
    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezados = next(filas)
    indices = [encabezados.index(ncolumna) for ncolumna in encabezados]
    arboleda = [{ ncolumna: fila[index] for ncolumna, index in zip(encabezados, indices)} for fila in filas]
    return arboleda

#Ejercicio 4.18
def medidas_de_especies(especies,arboleda):
    diccionario = { especie: [] for especie in especies}
    for especie in especies:
        medidas = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
        diccionario[especie] = medidas
    return diccionario

if __name__ == '__main__':
    ruta_archivo = '../data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(ruta_archivo)
    #Ejercicio 4.16
    #H1 = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    #Ejercicio 4.17
    H2 = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    print(H2)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    datos = medidas_de_especies(especies, arboleda)