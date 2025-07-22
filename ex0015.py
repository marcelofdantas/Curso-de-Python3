d = int(input('Dias alugados? '))
k = int(input('Km percorrido? '))
va = d * 60
vk = k * 0.15
print('O valor total do aluquel foi R$ {:.2f}'.format(va+vk))
