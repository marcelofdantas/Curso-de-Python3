l = float(input('A largura da parede? '))
a = float(input('A altura da parede? '))
area = l * a
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} m e sua area é de {} m2.\nSera necessario {} l de tinta para pintala. '.format(l, a, area, tinta))
