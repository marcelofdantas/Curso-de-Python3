'''Crie um programa que simule o funcionamento de um caixa eletrônico.
 No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
  e o programa vai informar quantas cédulas de cada valor serão entregues.
  OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

nota1 = nota10 = nota20 = nota50 = 0
valor = int(input('Qual valor do saque? '))
if valor >= 50:
    nota50 = valor // 50
    valor = valor % 50
if valor >= 20:
    nota20 = valor // 20
    valor = valor % 20
if valor >= 10:
    nota10 = valor // 10
    valor = valor % 10
if valor >= 1:
    nota1 = valor // 1
if nota50 > 0:
    print(f'Total de {nota50} notas de R$ 50,00')
if nota20 > 0 :
    print(f'Total de {nota20} notas de R$ 20,00')
if nota10 >0:
    print(f'Total de {nota10} notas de R$ 10,00')
if nota1 > 0:
    print(f'Total de {nota1} notas de R$ 1,00')'''

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Quanto vc quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break


