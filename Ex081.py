'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
lista.append(int(input('Digite um valor: ')))
r = input('Quer continuar? [S/N] ').upper().strip()[0]
while True:

    if r == 'N':
        break
    else:
        lista.append(int(input('Digite um valor: ')))
        r = input('Quer continuar? [S/N] ').upper().strip()[0]

print(f'Foram digitado {len(lista)} números.')
lista.sort(reverse=True)
print(f'Lista de forma ordenada decrescente: {lista}')

if 5 in lista:
    print(f'O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')