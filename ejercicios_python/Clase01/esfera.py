#Ejercicio 1.13
import math
#Solicito al usuario que ingrese por teclado
radio = input('Ingresá el radio para calcular el volumen de la esfera:')
print('El radio ingresado es', radio)
# volumen de la esfera 4/3 πr^3
pi = math.pi
volumen = 4/3 * pi * pow(int(radio), 3)
print('El volumen de la esfera es', volumen)