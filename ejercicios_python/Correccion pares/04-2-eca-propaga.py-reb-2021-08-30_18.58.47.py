#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 17:02:09 2021

@author: ~
"""
def propagar(lista):
    i = len(lista)
    m = 0
    encendidos = lista.copy()
    for c in range(0, i-1, 1):
        if encendidos[c] == 1 and encendidos[c+1] == 0:
            encendidos[c+1] = 1
    for k in range(i-1, 0, -1):
        if encendidos[k] == 1 and encendidos[k-1] == 0:
            encendidos[k-1] = 1
    return encendidos        

'''
Hola, tu código pasó todos los tests!
Como observaciones:
Quedó declarada una variable "m" que nunca fue usada, de todas formas no es relevante en el resultado del algoritmo
La función range por defecto avanza de a un valor, por lo tanto no sería necesario el tercer parámetro de range en el primer for
Pero en general me pareció muy claro el código y entendible :) 
Para ver otra resolución posible fijate que subieron en la clase 5 un video al respecto

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
