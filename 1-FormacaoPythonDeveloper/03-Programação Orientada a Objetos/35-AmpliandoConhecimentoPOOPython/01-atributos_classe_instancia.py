class Estudante:
    escola = 'Dio'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f'Nome: {self.nome}\t Matricula: {self.matricula} \tEscola: {self.escola}'
    


def mostrar_valores(*objetos):
    for objeto in objetos:
      print(objeto)

      
    
aluno1 = Estudante("Flavio", 1)
aluno2 = Estudante("Tamara", 3)

mostrar_valores(aluno1, aluno2)