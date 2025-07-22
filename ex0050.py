soma = 0
cont = 0
for c in range(1, 7):
    c = int(input('Digite um numero: '))
    if  c % 2 == 0:
        soma += c
        cont += 1
print(' A soma dos {} numeros pares é {}.'.format(cont, soma))