'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
 mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
maior = 0
menor = 0
soma = 0
media = 0
resp = 's'
cont =0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    soma += num
media = soma / cont
print('Voce digitou {} numeros tendo {} como media.'.format(cont, media))
print('O maior valor é {} e o menor valor é {}.'.format(maior, menor))