'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
 ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

total = c = cont = 0
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    resposta = input('Você quer continuar? [S/N] ').strip().upper()[0]

    total += preco

    if cont == 0:
        barato = preco
        nbarato = nome

    if preco > 1000:
        c += 1
    if barato > preco:
        barato = preco
        nbarato = nome
    if resposta == 'N':
        break
    cont += 1
print(f'O valor total da compra foi R${total:.2f}, {c} produto(s) custa(m) mais de R$1000 e o produto mais barato foi o(a) {nbarato}')
