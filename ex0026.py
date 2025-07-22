msg = str(input('Digite uma frase: ')).strip()
a = msg.lower().count('a')
a1 = msg.lower().find('a')+1
a2 = msg.lower().rfind('a')+1
print('A letra "a" aparece {} na frase.'.format(a))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(a1))
print('A letra "a" aparece pela ultima vez na posição {}.'.format(a2))
