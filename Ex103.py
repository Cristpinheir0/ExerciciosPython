'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado'''


def ficha(nome='(Não informado)', qtdgols=0):
    return print(f'O jogador {nome} fez {qtdgols} gols no campeonato')


n = input('Digite o nome do jogador: ')
g = input('Digite a quantidade de gols marcados: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(qtdgols=g)
else:
    ficha(n, g)

