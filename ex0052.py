n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n+1):
    if n % c ==0:
        print('\033[33m', end=' ')
        tot += +1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel por {} vezes.'.format(n, tot))
if tot == 2:
    print('É PRIMO')
else:
    print('Não é primo')