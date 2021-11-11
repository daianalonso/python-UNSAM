class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

#%% Ejercicio 9.12
class TorreDeControl:
    def __init__(self):
        '''Crea colas vacías'''
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, a):
        '''Encola a la cola de arribos'''
        self.arribos.encolar(a)
        
    def nueva_partida(self, p):
        '''Encola a la cola de partidas'''
        self.partidas.encolar(p)

    def ver_estado(self):
        if not self.arribos.esta_vacia():
            print(f"Vuelos esperando para aterrizar: {', '.join(self.arribos.items)}")
        if not self.partidas.esta_vacia():
            print(f"Vuelos esperando para despegar: {', '.join(self.partidas.items)}")

    def asignar_pista(self):
        if not self.arribos.esta_vacia():
            arribo = self.arribos.desencolar()
            print(f'El vuelo {arribo} aterrizó con éxito')
        elif not self.partidas.esta_vacia():
            partida = self.partidas.desencolar()
            print(f'El vuelo {partida} despegó con éxito')
        else:
            print(f'No hay vuelos en espera')
