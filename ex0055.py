maior = 0
menor = 0
nummaior = 0
nummenor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
        nummaior = c
        nummenor = c
    else:
        if peso > maior:
            maior = peso
            nummaior = c
        if peso < menor:
            menor = peso
            nummenor = c
print('O maior peso foi de {} kg da pessoa {}.'.format(maior, nummaior))
print('O menor peso foi de {} kg da pessoa {}.'.format(menor, nummenor))