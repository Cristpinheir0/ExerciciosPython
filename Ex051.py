'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.'''

a1 = float(input('Primeiro termo da PA:'))
r = float(input('Razão da PA:'))

for n in range(1, 11):
    an = a1 + ( n - 1 ) * r
    print('O {}º termo da PA é = {}'.format(n, an))