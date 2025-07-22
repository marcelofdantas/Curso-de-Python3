v = float(input('Qual a velocidade? '))
valor = (v-80)*7
if v > 80:
    print('Voce foi multado no valor de R$ {:.2f}'. format(valor))
else:
    print('Dentro do limite!!!!')
print('Dirija com cuidado!!!')
