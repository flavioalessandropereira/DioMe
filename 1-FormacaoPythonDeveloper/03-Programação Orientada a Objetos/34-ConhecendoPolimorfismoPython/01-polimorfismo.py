class Passaro:
    def voar(self):
        print('Voando ...')


class Pardal(Passaro):
    def voar(self):
        #return super().voar() #retornao metodo de voar que está no Passaro
        print('Pardal voa como nunca')


class Avestruz(Passaro):
    def voar(self):
        print('Avestruz Nao vao ..')


# Fixme: exemplo ruim do uso de harança para ganhar tempo
class Aviao(Passaro):
    def voar(self):
        print('Aviao decolando ...')


def plano_voo(objeto):
  objeto.voar()


p1 = Pardal()
p2 = Avestruz()

a1 = Aviao()

plano_voo(p1)
plano_voo(p2)

plano_voo(a1)