'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''


time = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',
'Flamengo', 'Vasco', 'Chapecoense', 'Atletico', 'Botafogo', 'Atletico-Pr',
'Bahia', 'Sao Paulo', 'Fluminense', 'Sport', 'Vitoria', 'Coritiba', 'Avai',
'Ponte Preta', 'Atletico-Go')
print(f'Nesse campeonato os 5 primeiros são:\n {time[0:5]}')
print(f'Os quatro ultimos são: \n{time[16:20]}')
print(f'Os times em ordem alfabetica são:\n{sorted(time)}')
print('Os time do campeonato são:')
for pos, clube in enumerate(time):
    print(f'{pos+1}. {clube}')
print(f'A Chapecoense ocupa a {time.index('Chapecoense')+1}º posição')