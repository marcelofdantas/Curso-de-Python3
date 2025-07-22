soma_idade = 0
media_idade = 0
maior_idadeh = 0
nome_hvelho = ''
mulher_menos20 = 0
for c in range(1, 5):
    print('----- {}º PESSOA -----'.format(c))
    nome = str(input('Qual o seu nome ? ')).strip()
    idade = int(input('Qual a sua idade ? '))
    sexo = str(input('Qual o seu sexo [M\F] ? ')).strip()
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        maior_idadeh = idade
        nome_hvelho = nome
    if sexo in 'Mm' and idade > maior_idadeh:
        maior_idadeh = idade
        nome_hvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menos20 += 1
media_idade = soma_idade / 4
print('A media de idade do grupo é de {:.2f} anos.'.format(media_idade))
print('O homem mais velho é {}. Com {} anos'.format(nome_hvelho,maior_idadeh))
print('{} mulheres tem menos de 20 anos.'.format(mulher_menos20))