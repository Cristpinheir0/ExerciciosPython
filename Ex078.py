'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista.'''
lista = list()
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c + 1}º número: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if maior < lista[c]:
            maior = lista[c]
        if menor > lista[c]:
            menor = lista[c]
print(f'Os cinco valores digitados foram: {lista}')
print(f'O menor valor digitado foi {menor} nas posições:',end = ' ')
for i, v in enumerate(lista):
    if v == menor:
        print(i, end = ' ')
print(f'\nO maior valor digitado foi {maior} nas posições:',end = ' ')
for i, v in enumerate(lista):
    if v == maior:
        print(i, end = ' ')

