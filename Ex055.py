'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

for c in range(1, 6):
    peso = int(input('Digite o peso da {}º pessoa:'.format(c)))

    if c == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso

print('O maior peso foi o de {}Kg e o menor foi o de {}Kg.'.format(maior, menor))