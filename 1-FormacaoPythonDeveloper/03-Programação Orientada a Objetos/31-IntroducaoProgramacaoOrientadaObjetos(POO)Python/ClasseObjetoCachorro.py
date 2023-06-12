class Cachorro:
  def __init__(self, nome, cor, acordado=True):
    self.nome = nome
    self.cor = cor
    self.acordado = acordado
  
  def latir(self):
    print('Auau')
  
  def dormir(self):
    self.acordado = False
    print('Zzzzz...')
      
# cao1 e cao2 seria os objetos
cao1 = Cachorro('Tequila', 'vermelha', False)
cao2 = Cachorro('Amora', 'branca e preto')

cao1.latir()

print(cao2.acordado)
cao2.dormir()
print(cao2.acordado)


