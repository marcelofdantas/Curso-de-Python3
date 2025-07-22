'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
 perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint
cont = 0
while True:
    print('VAMOS JOGAR PAR OU IMPAR')
    njog = int(input('Diga um valor: '))
    ncomp = randint(1, 10)
    soma = njog + ncomp
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('Par ou Impar? [P/I]')).upper().strip()[0]
    print(f'Voce jogou {njog} e o pc {ncomp}. Total {soma} ', end = '')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if jogador == 'P':
        if soma % 2 == 0:
            cont += 1
            print('PARABENS VOCE VENCEU!!! ')
        else:
            print('VOCE PERDEU!!!')
            break
    elif jogador == 'I':
        if soma % 2 == 1:
            cont += 1
            print('PARABENS VOCE VENCEU!!!')
        else:
            print('VOCE PERDEU!!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Voce venceu {cont} vezes.')

