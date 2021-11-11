# -*- coding: utf-8 -*-
"""
@author: Abril

@mail: abrilmpalacin@gmail.com
"""
'''
def propagar(lista):
	for i, f in enumerate(lista):
		if i-1>=0:
			if f==0 and lista[i-1]==1:
				lista[i] = 1

	for i in range(len(lista)-1, -1, -1):
		if i+1<len(lista):
			if lista[i]==0 and lista[i+1]==1:
				lista[i] = 1
	return lista
'''
def propagar(lista):
	for i, f in enumerate(lista):
		if i-1>=0:
			if f==0 and lista[i-1]==1:
				lista[i] = 1
		if i+1 < len(lista):
			if f == 0 and lista[i+1]==1:
				lista[i] = 1
	return lista

'''
Hola, tu código pasó todos los tests!
Como observaciones:
Tu función modifica la lista, no fue aclarado en el enunciado, pero si quisieras despues de ejecutar el algoritmo obtener la lista original antes de propagar no podrías
Para ver otra resolución posible fijate que subieron en la clase 5 un video al respecto

Como comentario de la entrega dijiste que te gustaria saber como resolver el ejercicio de árboles.
Te invito a que intentes hacerlo y te comparto el código que yo hice https://drive.google.com/drive/folders/1PLduNTddsjfCAr4UHvbcsgWrj7N9lMqo?usp=sharing
'''
lista_1 = [ 0, 0, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 0, 0, -1]
lista_3 = [ 0, 0, 0, 0, 0, 1]
lista_4 = []
lista_5 = [ 0 for _ in range(1000) ] + [1]
lista_6 = [1] + [ 0 for _ in range(1000) ]
lista_7 = [ (i% 6)//2-1 for i in range(200) ]
lista_8 = [ -1*((i% 6)//2-1) for i in range(60) ]

lista_7_res = [1 if x == 0 else x for x in lista_7]
lista_8_res = [1 if x == 0 else x for x in lista_8]

assert(propagar(lista_1) == [1,1,1,1,1,1]) 
assert(propagar(lista_2) == [ 0, 0, 0, 0, 0, -1])
assert(propagar(lista_3) == [1,1,1,1,1,1])
assert(propagar(lista_4) == [])
assert(propagar(lista_5) == [1 for _ in range(1001)])
assert(propagar(lista_6) == [1 for _ in range(1001)])
assert(propagar(lista_7) == lista_7_res)
assert(propagar(lista_8) == lista_8_res)