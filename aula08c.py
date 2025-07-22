import math
ca = float(input('Valor do Cateto Adjacente: '))
co = float(input('Valor do Cateto Oposto: '))
pca = ca**2
pco = co**2
sp = pca+pco
h = math.sqrt(sp)
print ('O valor da Hipotenusa é: {:.4f}'.format(h))