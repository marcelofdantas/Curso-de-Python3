'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo<=3:
    print('Carro novo')
else:
    print('Carro velho')
print('----FIM----')

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo<=3 else 'Carro velho')
print('----FIM----')

nome = str(input('Qual o seu nome? '))
if nome == 'marcelo':
    print('Que nome lindo voce tem.')
else:
    print('Que nome feio!!!')
print('Bom dia, {}'.format(nome))'''

n1 = float(input('Digite a primeira nota? '))
n2 = float(input('Digite a segunda nota? '))
m = (n1 + n2)/2
if m <= 7:
    print('A sua media foi {}, e voce foi REPROVADO!'.format(m))
else:
    print('A sua media foi {}, e voce foi APROVADO'.format(m))
print('Obrigado!!!')

