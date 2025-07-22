'''for c in range(0,6):
    print('Oi')
print('Fim')
for c in range(1,6):
    print(c)
for c in range(5,1,-1):
    print(c)
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)'''
s = 0
for c in range(0,4):
    n = int(input('Digite um numero: '))
    s += n #= s = s+n
print('A soma é {}.'.format(s))
