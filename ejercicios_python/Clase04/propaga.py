#Ejercicio 4.6
def propagar(unosyceros):
    n = len(unosyceros)
    for i in range(n-1):
        if unosyceros[i] == 1:
            if unosyceros[i+1] == 0:
                unosyceros[i+1] = 1
    for j in range(n-1,0,-1):
        if unosyceros[j] == 1:
            if unosyceros[j-1] == 0:
                    unosyceros[j-1] = 1
    return unosyceros
                        
if __name__ == '__main__':
    print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
    print(propagar([ 0, 0, 0, 1, 0, 0]))