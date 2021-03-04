'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.'''

a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
c = 0
while c != 11:
    an = a1 + c * r
    print('O {}º termo da PA é = {}'.format(c, an))
    c = c + 1
