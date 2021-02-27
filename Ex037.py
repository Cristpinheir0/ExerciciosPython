'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

n = int(input('Digite um número inteiro:'))
conv = int(input('Qual é a conversão desejada: (1)Binário, (2)Octal ou (3)Hexadecimal:'))

if 1 < conv > 3:
    conv = int(input('Qual é conversão desejada: (1)Binário, (2)Octal ou (3)Hexadecimal:'))

elif conv == 1:
    print('{} para binário é = {}'.format(n, bin(n)[2:]))

elif conv == 2:
    print('{} para Octal é = {}'.format(n, oct(n)[2:]))

else: #conv == 3
    print('{} para Hexadecimal é = {}'.format(n, hex(n)[2:]))
