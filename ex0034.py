s = float(input('Qual o seu salario?'))
if s <= 1250:
    sn = s*1.15
    print('O seu novo salario é R$ {:.2f}. Seu aumento foi de R$ {:.2f}.'.format(sn, (sn-s)))
else:
    sn2 = s*1.1
    print('O seu novo salario é R$ {:.2f}. Seu aumento foi de R$ {:.2f}'.format(sn2, (sn2-s)))
