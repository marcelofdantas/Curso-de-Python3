'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
 cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos'''


maior = homens = mulher_menor = 0
while True:
    print('-' * 26)
    print('\33[1;34m   CADASTRO DE PASSOAS\33[m')
    print('-' * 26)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if cont == 'N':
        break
print(f'São {maior} maiores que 18 anos, {homens} homens e\n{mulher_menor} mulheres menores que 20 anos.')
