'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120

fat = 1
num = int(input('Digite um numero para calcular seu fatorial: '))
print('Calculando {}!  '.format(num))
while num != 0:
    print('{} '.format(num), end='')
    print('x 'if num > 1 else '= ',end='')
    fat = fat * num
    num -= 1
print('{}.'.format(fat))'''
fat = 1
num = int(input('Digite um numero: '))
for num in range(num, 0, -1):
    print('{} '.format(num), end='')
    print('x 'if num > 1 else '= ',end='')
    fat = fat * num
print('{}.'.format(fat),end='')
