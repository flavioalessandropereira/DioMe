import itertools

resultado = itertools.permutations('abcdef', 5)
contador = 0
for i in resultado:
    contador += 1
    print(contador)
    print(i)
    print(f''.join(i)) #juntar os caracteres
    print("-="* 10)