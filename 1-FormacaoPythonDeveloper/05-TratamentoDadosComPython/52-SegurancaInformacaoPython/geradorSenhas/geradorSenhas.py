import random
import string

tamanho = int(input('Digite o tamnho de senha que vc deseja: '))

chars = string.ascii_letters + string.digits + '!@#$%^&*())_=+,.;?'

rnd = random.SystemRandom() #os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho)))
