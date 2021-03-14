'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep

def contador(i, f, p):
    print(f'\nContagem de {i} até {f}, de {p} em {p}:')
    if i > f:
        c = i
        while c >= f:
            print(c, end=' ')
            sleep(0.3)
            c -= p
    else:
        c = i
        while c <= f:
            print(c, end=' ')
            sleep(0.3)
            c += p


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('\nAgora é sua vez.\nDigite o início: ')), int(input('Digite o final:')), int(input('De quanto em quanto: ')))
