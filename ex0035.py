a = float(input('Valor reta A: '))
b = float(input('Valor reta B: '))
c = float(input('Valor reta C: '))

if a+b>c and a+c>b and b+c>a:
    print('Essas retas podem formar um triangulo')
else:
    print('Essas retas não formam um triangulo')

