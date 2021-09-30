#Ejercicio 3.17
print(f'{str(0):>6s}',end='')
for i in range(1,10):
    print(f'{i:>4d}',end='')
print('')
rayas = '-'*43
print(rayas)
for n in range(10):
    print(f'{n}:', end='')
    valor = 0
    print(f'{valor:>4d}', end='')
    for x in range(1,10):
        valor += n
        print(f'{valor:>4d}', end='')
    print('')