#Ejercicio 2.7
def buscar_precio(fruta):
    precio = 0.0
    with open('../Data/precios.csv', 'rt') as f:
        encontrado = False
        for line in f:
            fila = line.split(',')
            if fila[0] == fruta:
                 precio = float(fila[1])
                 encontrado = True
        if encontrado == False:
            print(f'{fruta} no figura en el listado de precios')                
        else:
            print(f'El precio de un cajón de {fruta} es: {precio}')

buscar_precio('Frambuesa')

