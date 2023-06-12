class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe ...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


    def falar(self):
        print('Auauau')


    def __del__(self):
        print('Removendo a instância da classe.')

def criar_cachorro():
    c = Cachorro('Joshep', 'Preto e branco', False)
    print(c.nome)

# c = Cachorro("Tequila", "Vermelha")
# c.falar()

criar_cachorro()