#Ejercicio 4.15
#%%
import csv
import os
import matplotlib.pyplot as plt
import numpy as np

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

#Ejercicio 5.26
def scatter_hd(lista_de_pares):
    datos = np.array(lista_de_pares)
    d = [t[0] for t in datos]
    h = [t[1] for t in datos]
    colors = np.random.rand(len(d)) 
    plt.scatter(d,h, c=colors, alpha=0.5)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()

def scatter_especies(dicc_pares):
    for especie in dicc_pares:
        datos = np.array(dicc_pares[especie])
        d = [t[0] for t in datos]
        h = [t[1] for t in datos]
        colors = np.random.rand(len(d)) 
        plt.scatter(d,h, c=colors, alpha=0.5)
        plt.xlabel("diametro (cm)")
        plt.xlim(0,30)
        plt.ylim(0,160)
        plt.ylabel("alto (m)")
        plt.title(f'Relación diámetro-alto para {especie}')
        plt.show()

if __name__ == '__main__':
    os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    scatter_especies(medidas)
# %%
