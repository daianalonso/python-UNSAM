#%% Ejercicio 11.13
def medidas_hoja_A(N):
    ''' Para un valor N > 0 devuelve el ancho y largo de una hoja A(N)'''
    if N == 0: #Caso base: ancho y largo hoja A0
        return (841, 1189) 
    else:
    #La hoja de la medida con el numero más alto resulta de doblar a la mitad por el largo la hoja anterior
        return (medidas_hoja_A(N-1)[1]//2, medidas_hoja_A(N-1)[0])