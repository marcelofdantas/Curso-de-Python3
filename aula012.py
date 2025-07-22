nome = str(input('Digite seu nome: '))
if nome == 'Marcelo':
    print('Que nome bonito')
elif nome == 'João' or nome == 'Pedro' or nome == 'Paulo':
    print('Que nome comum')
else:
    print('Tenha um bom dia!!!{}'.format(nome))