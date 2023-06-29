from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome="Tequila", idade=14)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Tequila').first()
    if pessoa is not None:
        print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Flavio').first()
    pessoa.nome = 'Felipe'
    # pessoa.idade=19
    pessoa.save()

def exlui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Tequila').first()
    if pessoa is not None:
        pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)


if __name__ == '__main__':
    insere_usuario('tamara','333')
    insere_usuario('joaquim', '321')
    consulta_todos_usuarios()
    # insere_pessoas()
    #altera_pessoa()
    # exlui_pessoa()
    # consulta_pessoas()
