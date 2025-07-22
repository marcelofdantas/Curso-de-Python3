'''Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

total = 0
maismil = 0
pbarato = 0
nbarato = 0
print('='*23)
print('\33[1;33m   LOJA SUPER BARATÃO\33[m')
print('='*23)

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    if preco >= 1000:
        maismil += 1
    '''if total == preco:
        pbarato = preco
        nbarato = nome.upper()
    if pbarato > preco:
        pbarato = preco
        nbarato = nome.upper()'''
    if total == preco or pbarato > preco:
        pbarato = preco
        nbarato = nome.upper()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O valor das compras é de {total} reais.')
print(f'{maismil} produtos custam mais de mil reais.')
print(f'{nbarato} é o produto mais barato. Custando {pbarato} reais ')