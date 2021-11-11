#%% Ejercicio 8.5
import os
import sys

def archivos_png(directorio):
    en_formato_png =[]
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name[-3:] == 'png':
                en_formato_png.append(name)
    return en_formato_png


if __name__ == '__main__':
    try:
        archivos_png(sys.argv[1])
    except:
        print('El formato es listar_imgs.py <ruta_carpeta>')
