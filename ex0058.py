'''import random
from time import sleep
cont = 1
nc = random.randint(0, 10)
np = int(input('Digite um numero de 0 a 10: '))
print('Pensando....')
sleep(1)
if nc == np:
    cont = 1
while np != nc:
    if np > nc:
        print('Menos. Voce perdeu. Tente novamente')
        np = int(input('Digite um numero de 0 a 10: '))
        print('Pensando....')
        sleep(1)
        cont += 1
    elif np < nc:
        print('Mais. Voce perdeu. Tente novamente')
        np = int(input('Digite um numero de 0 a 10: '))
        print('Pensando....')
        sleep(1)
        cont += 1
print('Parabens vc VENCEU!!!!! com {} tentativas'.format(cont))'''

from random import randint
nc = randint(0, 10)
acertou = False
palpites = 0
print('Eu sou o seu computador e pensei em um numero de 0 a 10.')
print('Sera que vc adivinha qual foi? {}'.format(nc))
while not acertou:
    jogador = int(input('Digite um Numero entre 0 e 10:'))
    palpites += 1
    if jogador == nc:
        acertou = True
    else:
        if jogador > nc:
            print('Digite um numero menor.')
        elif jogador < nc:
            print('Digite um numero maior.')
print('Voce venceu com {} palpites.'.format(palpites))
