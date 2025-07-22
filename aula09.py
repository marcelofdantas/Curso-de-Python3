'''quebrar linhas
obs. primeiro numero é onde comeca, segundo onde termina -1 e teceiro pula de x em x'''

frase =  'Curso em Video de Python'
print(frase[9::3])
print(frase[2:14])
print(frase[2:20:2])

'''Analise
len=comprimento
count=contar
find=encontrar(posiçao onde começa)
in=existe'''

len(frase)
print(len(frase))
frase.count('o')
print(frase.count('o'))
print(frase.count('o',2, 16))
print(frase.find('deo'))
print(frase.find('android1'))
print('Curso'in frase)

'''transformação
replace=trocar/substituir
upper=pra cima/maiusculo
lower=pra baixo/ minusculo
capitalize=joga pra minusculo tudo e deixa primeira em maiusculo
title=joga tudo pra minusculo e deixa primeira de cada palavra maiuscula
strip=remove espacos inuteis
rstrip=remove os espacos inuteis da direita
lstrip=esquerda'''

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

'''divisão
split=divisao em palavras'''

print(frase.split())

'''junção
join=junta palavras'''

print('-'.join(frase))
