peso = float(input('Qual o seu peso? '))
alt = float(input('Qual a sua altura? '))
imc = peso/(alt**2)
print('Seu IMC é {:.2f}.'.format(imc))
if imc < 18.5:
    print('GRILO. Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Baleia. Super gordo.')
