'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

lista = []
listag = []
maior = men = 0

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    listag.append(lista[:])  # Copiando Lista e a colando dentro de listag.
    if len(listag) == 0:
        maior = men = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < men:
            men = lista[1]
    lista.clear()

    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break
print(men)
print(f'Dados cadastrados: {listag}')
print(f'Foram cadastradas {len(listag)} pessoas.')
print(f'O maior peso cadastrado foi {maior}Kg.', end=' ')

for p in listag:
    if p[1] == maior:
        print(p[0])

for p in listag:
    if p[1] == men:
        print(p[0])
print(f'O menor peso cadastrado foi {men}Kg.', end=' ')
