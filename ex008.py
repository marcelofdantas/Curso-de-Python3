n = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a \n{:.3f}Km \n{:.2f}Hm \n{:.1f}Dam \n{:.0f}Dm \n{:.0f}Cm \n{:.0f}Mm'.format(n, (n/1000), (n/100), (n/10), (n*10), (n*100), (n*1000)))
