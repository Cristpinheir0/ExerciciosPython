'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.'''

n = int(input('Digite um número: '))
resposta = input('Quer continuar[S/N]: ').strip().upper()[0]
soma = n
maior = n
menor = n
c = 1

while resposta != 'S' and resposta != 'N':
    resposta = input('Resposta incorreta. Digitar [S/N]: ').strip().upper()[0]
while resposta == 'S':
    n = int(input('Digite um número: '))
    c += 1
    soma += n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    resposta = input('Quer continuar[S/N]: ').strip().upper()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = input('Resposta incorreta. Digitar [S/N] ').strip().upper()[0]
media = soma / c
print('A média dos valores digitados é de {}, o maior valor foi {} e o menor foi {}.'.format(media, maior, menor))
