'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''


def área(l, c):
    a = l * c
    print(f'A área do terreno é: {a:.2f}m^2')


área(float(input('Digite a largura do terreno: ')), float(input('Digite o comprimento do terreno: ')))
