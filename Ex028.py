''' Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint

tentativa = int(input('Tente descobrir o número sorteado de 0 a 5:'))
num = randint(0, 5)

if tentativa == num:
    print('Parabéns você acertou o número sorteado: {}'.format(num))
else:
    print('Você não acertou o número sorteado: {}'.format(num))