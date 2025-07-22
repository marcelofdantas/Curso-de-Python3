import datetime
nasc = int(input('Digite o ano que voce nasceu: '))
dh = datetime.date.today().year
idade = dh - nasc
print('Voce tem {} anos!'.format(idade))
if idade < 18:
    print('Ainda não esta no prazo de voce se alistar, faltam {} anos.'.format(18-idade))
elif idade == 18:
    print('Esta na hora de voce se alistar.')
else:
    print('Voce ja passou da idade de se alistar. Era pra ter feito a {} anos atras.'.format(idade-18))


