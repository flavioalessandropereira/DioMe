numeros = set ([1,2,3,1,3,4])
print (numeros)


letras = set('abacaxi')
print (letras)


carros = set(('palio', 'celta', 'gol', 'palio'))
print(carros)

linguagens = {'PYTHON', 'JAVA', 'PYTHON'}
print(linguagens)


## convertendo set para lista

numeros = {1,2,3,2}
numeros = list (numeros)
print(numeros[0])

##iterar o set dento do for
carros = { 'palio', 'celta', 'gol'}

for carro in carros:
    print(carro)

##iterar o set dento do for e enumerar
carros = { 'palio', 'celta', 'gol'}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



## {}.union
conj_a = {1,2}
conj_b = {3,4}
print(conj_a.union(conj_b))


## {}.intersection
conj_a = {1,2,3,4}
conj_b = {2,3,4}
print(conj_a.intersection(conj_b))

## {}.difference
conj_a = {1,2,3}
conj_b = {2,3,4}
print(conj_a.difference(conj_b))
print(conj_b.difference(conj_a))


## {}.symmetric_difference
conj_a = {1,2,3}
conj_b = {2,3,4}
print(conj_a.symmetric_difference(conj_b))
