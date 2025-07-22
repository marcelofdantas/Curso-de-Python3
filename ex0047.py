s = 0
print('Os numeros pares entre 1 e 50 são:')
for c in range(0, 51, 2):
    print(c)
    s += c
print('A soma deles é: {}.'.format(s))