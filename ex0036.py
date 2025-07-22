valor = float(input('Qual o valor da casa? '))
renda = float(input('Qual o seu salario? '))
tempo = int(input('Em quantos meses sera o prazo de pagamento? '))
pm = valor/tempo
r = (pm*100)/renda
if r <= 30:
    print('Parabens!! Seu credito foi aprovado.\nSua parcela sera de R${:.2f} durante {} meses.'.format(pm,tempo))
else:
    print('Infelizmente seu financiamento foi negado pois o valor da parcela R$ {:.2f},\n corresponde a {:.2f}% do seu salario e o limite maximo é 30%'.format(pm, r))

