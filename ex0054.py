from datetime import date
atual = date.today().year
idade = 0
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Qual ano voce nasceu? '))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade e {} pessoas sao menores. '.format(maior, menor))
