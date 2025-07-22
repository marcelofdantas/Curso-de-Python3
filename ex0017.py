import math
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = math.hypot(ca, co)
print('Em um triangulo retangulo com cateto oposto {} e cateto adjacente {}\n a hipotenusa é {:.3f}'.format(ca,co,h))
