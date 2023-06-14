class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    # mais automático para ver a classe, se adicionar vai aparecer automaticamente
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Manifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)



class Gato(Manifero):
    pass

class FalarMixin:
    def falar(self):
       return 'Estou falando'


class Ornitorrinco(Manifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.__mro__) # __mro__, ordem de resolucao
        print(Ornitorrinco.mro())

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)





gato= Gato(nro_patas =4, cor_pelo ='preto')
print(gato)


ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo='vermelho', cor_bico='laranja') #usando **kw precisa informar, chave=valor Exemplo: cor_pelo = 'vermelho'
print(ornitorrinco)
print(ornitorrinco.falar())
