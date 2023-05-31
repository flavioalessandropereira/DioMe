frutas = ['laranja', 'maca', 'uva']
print(frutas)

frutas =[] #frutas está vazia
print(frutas)

letras = list('python')
print (letras)

numeros = list(range (10))
print(numeros)

carro = ['ferrari1','F8', 4200, 43.223,"São Paulo", True]
print(carro)

#filtro
numeros = [1,20,31,2,8,65,85]
pares = []

for numero in numeros:
  if numero %2 == 0:
    pares.append(numero)
    print(numero)