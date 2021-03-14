'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

placar = {'jogador 1': randint(1, 6),
          'jogador 2': randint(1, 6),
          'jogador 3': randint(1, 6),
          'jogador 4': randint(1, 6)}
colocação = []

for k, v in placar.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
colocação = sorted(placar.items(), key=itemgetter(1), reverse=True)
print('')
for i, v in enumerate(colocação):
    print(f'Em {i+1}º ficou o {v[0]} com {v[1]}')
    sleep(0.5)
