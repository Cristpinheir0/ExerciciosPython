'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
 vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
 pares sorteados pela função anterior.'''

from random import randint
from time import sleep

def sorteia(lista):
    for c in range(1,6):
        lista.append(randint(0,10))

    print('Os 5 números sorteados foram: ',end = '')

    for c in lista:
        sleep(0.3)
        print(c, end = ' ')


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'\nA soma dos números pares sorteados é =',end = ' ')
    print(f'{soma}')


números = []
sorteia(números)
somaPar(números)
