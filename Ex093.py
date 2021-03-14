'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

from time import sleep

jogador = {'nome': str(input('Digite o nome do jogador: '))}
qtdpartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
gols = []
total = 0
for c in range(0, qtdpartidas):
    gols.append(int(input('Quantos gols foram marcados: ')))
    total += gols[c]

jogador['gols'] = gols[:]
jogador['total'] = total

print(jogador.items())
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
sleep(1)
print(f'O jogador {jogador["nome"]} jogou {qtdpartidas} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, marcou {v}')
    sleep(0.25)
