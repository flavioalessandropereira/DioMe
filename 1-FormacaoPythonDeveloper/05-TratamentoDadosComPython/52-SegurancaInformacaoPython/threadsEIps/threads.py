import time
from threading import Thread


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto: {piloto} km {trajeto}\n')


th_carro1 = Thread(target=carro, args=[1, 'Felipe'])
th_carro2 = Thread(target=carro, args=[2, 'Flavio'])

th_carro1.start()
th_carro2.start()
