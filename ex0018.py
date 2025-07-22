import math
an = int(input('Digite um angulo: '))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))
print('Para um angulo de {} o seno é {:.2}, o cosseno é {:.2} e a tangente é {:.2}.'.format(an, s, c, t))

