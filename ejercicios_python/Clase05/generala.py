import random
#Ejercicio 5.1
#Devuelve true si todos los dados de la tirada son iguales
def es_generala(tirada):
    return tirada.count(tirada[0]) == len(tirada)

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada

#Ejercicio 5.2
def prob_generala(N):
    x = 0
    for n in range(0,N):
        if es_generala(tirar()) == True:
            x += 1
    return (x/N)


if __name__ == '__main__':
    N = 100000
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
