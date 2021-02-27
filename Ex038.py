'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))

if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O segundo número é maior.')
else: #n1 == n2
    print('Não existe valor maior, ois dois são iguais.')