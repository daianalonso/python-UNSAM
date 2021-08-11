#Ejercicio 1.18
cadena = input('Escriba la palabra:')
capadepenapa = ''
for c in cadena:
    capadepenapa = capadepenapa + c
    if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
    	capadepenapa = capadepenapa + 'p' + c
print(capadepenapa)
#Output obtenido:
#Geperipingoposopo