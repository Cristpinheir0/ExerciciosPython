'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag)'''

n = int(input('Digite um número(999 para sair do programa): '))
c = 0
soma = 0
while True:
    if n == 999:
        break
    soma += n
    c += 1
    n = int(input('Digite um número(999 para sair do programa): '))

print(f'Foram digitados {c} números e a soma deles foi {soma}')