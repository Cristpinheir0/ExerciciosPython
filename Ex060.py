'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

num = int(input('Digite um número: '))
c = num - 1
fat = num
while c != 1:
    fat = fat * c
    c = c - 1
print('O fatorial de {} é {}'.format(num, fat))