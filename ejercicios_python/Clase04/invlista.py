#Ejercicio 4.5
def invertir_lista(lista):
    invertida = []
    for e in lista: 
        invertida.insert(0,e) #Inserto en la posicion 0 (primero)
    return invertida

if __name__ == '__main__':
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))