import math

a = float(input('Digite  um angulo:'))

sn = math.sin(math.radians(a))
cs = math.cos(math.radians(a))
tg = math.tan(math.radians(a))

print('O sena= {:.2}, cosa= {:.2} e tga= {:.2f}'.format(sn, cs, tg))
