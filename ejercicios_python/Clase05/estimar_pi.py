import random

#Ejercicio 5.5
def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def estimar_pi(N):
    puntos = [generar_punto() for i in range(N)]
    puntos_dentro = [(x,y) for x, y in puntos if pow(x,2) + pow(y,2) < 1]
    pi = 4*(len(puntos_dentro))/N
    return pi

if __name__ == '__main__':
    print(estimar_pi(100000))
