'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla'''

from random import randint
maior = menor = 0
num = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100))
print(f'Os numeros gerados foram: \n{num}')
print(f'O menor valor é {max(num)}.')
print(f'O maior valor é {min(num)}.')