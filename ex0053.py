f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
junto = ''.join(p)
inv = ''
for letra in range(len(junto)-1, -1, -1):
    inv += junto[letra]
print('O inverso de {} é {}.'.format(f, inv))
if f == inv:
    print('Temos um palindromo')
else:
    print('Nao temos um palindromo')
