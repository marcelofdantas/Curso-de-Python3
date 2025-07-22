valor = float(input('Qual o valor dos produtos? '))
fp = int(input('''Qual sera a forma de pagamento?
Escolha:
[ 1 ] - Dinheiro/Cheque
[ 2 ] - Cartão 
'''))
if fp == 1:
    print('Dinheiro/Cheque')
    pf = valor*0.9
    print('Pague R$ {:.2f}'.format(pf))
else:
    print('Cartão')
    prazo = int(input('''Qual o prazo?
    Escolha:
    [ 1 ] - Avista
    [ 2 ] - 2X
    [ 3 ] - 3X ou mais 
    '''))
    print('Sua escolha: {}'.format(prazo))
    if prazo == 1:
        print('Pague R$ {:.2f}.'.format(valor*0.95))
    elif prazo == 2:
        print('Pague R$ {:.2f}. Em 2 x de R$ {:.2f}.'.format(valor, (valor/2)))
    elif prazo == 3 :
        np = int(input('Quantas parcelas: '))
        vp = (valor*1.2)/np
        print('Pague R$ {:.2f}. Em {} x de R$ {:.2f}.'.format(valor*1.2, np, vp))
print('Obrigado')


