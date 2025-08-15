'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite um numero: ')),
int(input('Digite um numero: ')),
int(input('Digite um numero: ')),
int(input('Digite um numero: ')))
print(f'Voce digitou:\n{num}')
print(f'O numero 9 apareceu {num.count(9)} vez')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição.')
else:
    print('O valor 3 não foi digitado.')
for n in num:
    if n % 2 == 0:
        print(n , end=' ,')
print(' são pares')