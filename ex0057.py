sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
while sexo not in 'MmFf':
    sexo = str(input('Opção invalida. Digite M ou F.')).strip().upper()[0]
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print('O sexo é {}'.format(sexo))