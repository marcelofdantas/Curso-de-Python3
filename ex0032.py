from datetime import date
data = int(input('Digite o ano que quer analisar. Coloque 0 para ver o ano atual da maquina: '))
if data == 0:
    data = date.today().year
if data%4 ==0 and data%100 !=0 or data%400 == 0:
    print('{} é Bissexto'.format(data))
else:
    print('{} Não bissexto'.format(data))
