d = int(input('Qual da distancia em km? '))
if d <= 200:
    v = d*0.5
    print('O valor da viagem é R$ {}.'.format(v))
else:
    v2 = d*0.45
    print('O valor da viagem é RS {}.'.format(v2))
