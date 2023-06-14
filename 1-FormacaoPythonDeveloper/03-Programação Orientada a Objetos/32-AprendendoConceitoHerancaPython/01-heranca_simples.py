class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
       self.cor = cor
       self.placa = placa
       self.numero_rodas = numero_rodas

    def ligar_motor(self):
       print('Motor ligado ... Vrumm')


    # def __str__(self) -> str:
    #    return self.cor

    
    def __str__(self) -> str: # mais automático para ver a classe, se adicionar vai aparecer automaticamente
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass



class Carro (Veiculo):
  pass



class Caminhao (Veiculo):
    def __init__(self,cor, placa, numero_rodas, carregado):
       super().__init__(cor, placa, numero_rodas)
       self.carregado = carregado

    def esta_carregado(self):
       print(f"{'sim' if self.carregado else 'nao'} estou carregado")


moto = Motocicleta("verde", "BYB1202", 2)
print(moto)
moto.ligar_motor()


carro1 = Carro('vemelho', "PLR2323", 4)
print(carro1)

caminhao1 = Caminhao('Branco', 'RFR2312', 10, True)
caminhao1.ligar_motor()
print(caminhao1)
caminhao1.esta_carregado()