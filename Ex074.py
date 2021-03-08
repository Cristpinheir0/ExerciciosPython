'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

nums = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Números gerados:')

for n in nums:
    print(n, end = ' ')

#Poderia fazer uma repetição para encontrar o maior e o menor valor dentro de nums, mas existem duas funções, max() e min()
#Que irão mostrar qual é maior e o menor valor dentro de nums

print(f'\nO maior valor de {nums} é {max(nums)}')
print(f'O menor valor de {nums} é {min(nums)}')
