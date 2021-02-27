'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

l1 = float(input('Digite o comprimento do primeiro lado:'))
l2 = float(input('Digite o comprimento do segundo lado:'))
l3 = float(input('Digite o comprimento do terceiro lado:'))

if l1 == l2 and l1 == l3:
    print('É possível formar um triângulo, sendo um EQUILÁTERO.')

elif l1 != l2 and l1 != l3 and l2 != l3:
    if l1 < l2 + l3 and l2 < l1 +l3 and l3 < l1 + l2:
        print('É possível formar um triângulo, sendo um ESCALENO.')
    else:
        print('Não é possível montar nenhum triângulo.')
else:
    print('É possível formar um triãngulo, sendo um ISÓCELES.')