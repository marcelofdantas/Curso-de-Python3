s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s += c
print('A soma dos {} valores é {}.'.format(cont, s))
