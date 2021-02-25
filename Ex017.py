import math #Por usar apenas uma função pode-se fazer assim: from math import hypot, usando menos memoria

catop = float(input('Digite o comprimento do cateto oposto;'))
catad = float(input('Digite o comprimento do cateto adjacente:'))

hip = math.hypot(catop, catad)

print('O comprimento da hipotenusa é {}'.format(hip))