'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''


num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
opera = 0
while opera != 5:
   print('''Escolha a opção desejada:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa
    ''')
   opera = int(input('Qual opção? '))
   if opera == 1:
       soma = num1 + num2
       print('A soma é {}.'.format(soma))
   elif opera == 2:
       mult = num1 * num2
       print('A multiplicação é {}.'.format(mult))
   elif opera == 3:
       if num1 == num2:
           print('Não existe maior. Eles são iguais')
       elif num1 < num2:
           print('O maior é o segundo numero que é {}.'.format(num2))
       else:
           print('O maior numero é o primeiro que é {}.'.format(num1))
   elif opera == 4:
       print('Informe os numeros novamente')
       num1 = int(input('Digite o primeiro numero: '))
       num2 = int(input('Digite o segundo numero: '))
   elif opera == 5:
       print('Finalizando...')
   else:
       print('Opção invalida. Tente Novamente')
print('Volte sempre.')