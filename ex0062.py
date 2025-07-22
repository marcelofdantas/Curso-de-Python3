'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.'''


print('='*20)
print('\33[1;31m  TERMOS DE UMA PA:\33[m')
print('='*20)
cont = 0
termo1 = int(input('Digite o primeiro termo:'))
razao = int(input('Qual a razão:'))
termo = int(input('Quantos termos vc quer? '))
while mais != 0:
    termo += mais
    while cont < termo:
        print('{} -> '.format(termo1),end='')
        termo1 += razao
        cont +=1
    print('Pausa')
    mais = int(input('Quantos termos a mais voce quer mostrar? '))
print('Fim')
print('{} termos.'.format(cont))

