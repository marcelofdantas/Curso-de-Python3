'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
cont = 1
print('=' * 20)
print('\033[1;31m10 TERMOS DE UMA PA\33[m')
print('=' * 20)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
while cont < 11:
    print('{} -> '.format(termo),end='')
    termo += razao
    cont +=1
print('FIM')