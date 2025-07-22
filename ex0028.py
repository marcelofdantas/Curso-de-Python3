import random
from time import sleep

nc = random.randint(0, 5)
np  = int(input('Digite o numero igual ao do computador: '))
print('Pensando.....')
sleep(3)
if np == nc:
    print('VENCEDOR')
else:
    print('PERDEDOR')
print('Numero computador {}.'.format(nc))
