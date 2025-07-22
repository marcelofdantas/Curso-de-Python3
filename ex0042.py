a = float(input('Valor reta A: '))
b = float(input('Valor reta B: '))
c = float(input('Valor reta C: '))

if a+b>c and a+c>b and b+c>a:
    print('Essas retas podem formar um triangulo. ', end='')
    if a == b == c:
        print('Equilatero: Todos os lados iguais.')
    elif a == b or b == c or a == c:
        print('Isosceles: Dois lados iguais')
    elif a != b != c !=a:
        print('Escaleno: Todos os lados diferentes')
else:
    print('Essas retas não formam um triangulo')
