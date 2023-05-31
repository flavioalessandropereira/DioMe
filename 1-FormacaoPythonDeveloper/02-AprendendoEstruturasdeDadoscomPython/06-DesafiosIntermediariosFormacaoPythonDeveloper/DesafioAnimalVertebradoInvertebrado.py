# DESAFIO
# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

# Entrada
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

# Saída
# Imprima o nome do animal correspondente à entrada fornecida.
a = input() 
b = input() 
c = input() 

reposta = None

if a == 'vertebrado': 
  if b == 'ave' and c == 'carnivoro':
    resposta = 'aguia'
  elif b == 'ave' and c == 'onivoro':
    resposta = 'pomba'
  elif b == 'mamifero' and c == 'onivoro':
    resposta = 'homem'
  elif b == 'mamifero' and c == 'herbivoro':
    resposta = 'vaca'

elif a == 'invertebrado':
  if b == 'inseto' and c == 'hematofago':
    resposta = 'pulga'
  elif b == 'inseto' and c == 'herbivoro':
    resposta = 'lagarta'
  elif b == 'anelideo' and c == 'hematofago':
    resposta = 'sanguessuga'
  elif b == 'anelideo' and c == 'onivoro':
    resposta = 'minhoca'

print (resposta)