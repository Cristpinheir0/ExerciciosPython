'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Bragantino.'''

brasileirao = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
               'Athletico-PR', 'Bragantino', 'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife',
               'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

print(f'Os cinco primeiros colocados foram: {brasileirao[:5]}')
print(f'Os cinco últimos colocados foram: {brasileirao[14:]}')
print(f'Os times em ordem alfabética: {sorted(brasileirao)}')
c = 0
while True:
    if brasileirao[c] != 'Bragantino':
        c += 1
    else:
        break
    #Esse while pode ser trocado pela função .index(Chapecoense) ela irá dizer a posição que esse termo aparece
print(f'A posição em que o Bragantino ficou foi a {c + 1} posição')