n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
media = (n1 + n2)/2
print('Sua media foi {:.2f}'.format(media))
if media < 5.0:
    print('Voce é burro e foi REPROVADO.')
elif media >= 5.0 and media < 7.0:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
