from random import randint
from time import sleep
'''jog = int(input('Escolha:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n '))
if jog == 1:
    jog = 'Pedra'
elif jog ==2:
    jog = 'Papel'
else:
    jog = 'Tesoura'
    print(jog)
print('Agora é a minha vez:')
comp = randint(1,3)
sleep(1)
if comp == 1:
    comp = 'Pedra'
elif comp == 2:
    comp = 'Papel'
elif comp == 3:
    comp = 'Tesoura'
else:
    print('erro')
print(comp)
if jog == comp:
    print('Empate')
elif jog == 'Pedra' and comp == 'Papel':
    print('Pedra perde de Papel\n Voce PERDEU')
elif jog == 'Pedra' and comp == 'Tesoura':
    print('Pedra ganha de Tesoura.\nVoce VENCEU')
elif jog == 'Papel' and comp == 'Pedra':
    print('Papel ganha de Pedra\nVoce VENCEU')
elif jog == 'Papel' and comp == 'Tesoura':
    print('Papel perde de Tesoura\nVoce PERDEU')
elif jog == 'Tesoura' and comp == 'Pedra':
    print('Tesoura perde para Pedra.\nVoce PERDEU')
elif jog == 'Tesoura' and comp == 'Papel':
    print('Tesoura ganha de Papel.\nVoce VENCEU')
else:
    print('erro')'''
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
jog = int(input('''Escolha uma opção:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
'''))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
print('*='*15)
print('Voce escolheu {}.'.format(itens[jog-1]))
print('Computador escolheu {}.'.format(itens[comp]))
print('*='*15)
if comp == jog-1:
    print('EMPATE')
elif comp == 0:#Pedra
    if jog == 2:#Papel
        print('Voce VENCEU.\nPapel ganha de Pedra')
    elif jog == 3:#Tesoura
        print('Voce PERDEU.\nTesoura perde para Pedra')
elif comp == 1:#Papel
    if jog == 1:#Pedra
        print('Voce PERDEU.\nPedra perde de Papel')
    elif jog == 3: #Tesoura
        print('Voce GANHOU.\nTesoura ganha de Papel')
elif comp == 2:#Tesoura
    if jog == 1:#Pedra
        print('Voce GANHOU.\nPedra ganha de Tesoura')
    elif jog == 2: #papel
        print('Voce PERDEU.\nPapel perde de Tesoura')
else:
    print('erro')

