#Ejercicio 2.14
def a_geringoso(palabra):
    capadepenapa = ''
    for c in palabra:
        capadepenapa += c
        if c in 'aeiou':
            capadepenapa += 'p' + c
    return capadepenapa

def diccionario_geringoso(lista):
    d = dict.fromkeys(lista, '')
    for palabra in lista:
        d[palabra] = a_geringoso(palabra)
    return d

print(diccionario_geringoso(['banana', 'manzana', 'mandarina']))

