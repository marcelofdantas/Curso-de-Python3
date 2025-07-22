''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão.'''
print('='*20)
print('\33[1;36m10 TERMOS DE UMA PA\33[m')
print('='*20)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(pt, pt+(10*razao), razao):
    print(c, end=' -> ')
print('Fim')