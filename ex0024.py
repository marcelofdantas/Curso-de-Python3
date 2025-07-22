cidade = str(input('Digite o nome da sua cidade: ')).strip()
sim = cidade.lower().split()[0]
print(cidade[:5].upper() == "SANTO" )
print('O primeiro nome da sua cidade começa com santo? {}'.format('santo'in sim))