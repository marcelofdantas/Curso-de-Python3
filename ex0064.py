'''Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''

cont = 0
soma = 0
num = int(input('Digite um numero:'))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite outro numero ou 999 para sair: '))
print('A soma dos {} digitados é {}.'.format(cont, soma))


