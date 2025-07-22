import datetime
an = int(input('Em que ano voce nasceu? '))
dh = datetime.date.today().year
idade = dh - an
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')