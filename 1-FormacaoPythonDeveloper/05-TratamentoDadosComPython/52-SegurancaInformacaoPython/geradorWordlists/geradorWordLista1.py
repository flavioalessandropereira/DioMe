import itertools

string = input('Stringa a ser permutada: ')
resultado = itertools.permutations(string, len(string))
contador = 0

for i in resultado:
    contador += 1
    print(contador)
    print(i)
    print(f''.join(i)) #juntar os caracteres
    print("-="* 10)