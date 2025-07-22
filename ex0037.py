n = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ]converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido em BINARIO é {}.'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção invalida')
