'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

jogos = []
separados = []
q = int(input('Quantos jogos serão feitos? '))

for j in range(0, q):
    for n in range(0, 6):
        v = randint(1, 60)
        if v not in separados:
            separados.append(v)
        separados.sort()
    print(f'O {j+1}º jogo foi: {separados}')
    sleep(1)
    jogos.append(separados[:])
    separados.clear()
print(f'Os jogos foram: {jogos}')