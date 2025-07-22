s = float(input('Valor do salario atual: R$ '))
a = float(input('Digite o valor do percentual de aumento: '))
p = 1 + (a/100)
sn = s * p
g = (s*p) - s
print('O salario era de R$ {:.2f} e teve um aumento de {:.2f} %. \nO novo salario é de R$ {:.2f} \nSeu aumento foi de R$ {:.2f}'.format(s, a, sn, g))



