class Lote:
    def __init__(self, name, number, price):
        self.nombre = name
        self.cajones = number
        self.precio = price
    
    #%%Ejercicio 9.9
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
        
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, cant):
        self.cajones -= cant 