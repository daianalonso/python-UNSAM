#Ejercicio 10.3
class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])
    
    def __len__(self):
        return len(self.lotes)

    def __getitem__(self, idx):
        return self.lotes[idx]

    def __repr__(self):
        return f'Camion({self.lotes})'
    
    def __str__(self):
        t = [ 'Camion con ' + str(len(self.lotes)) +' lotes:' ]
        for obj in self.lotes:
            s = f'Lote de {obj.cajones} cajones de {obj.nombre}, pagados a ${obj.precio} cada uno.'
            t.append(s)
        return '\n'.join(t)

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total