'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. '''

pares = []
impares = []
lista = [[pares],[impares]]

for c in range(0, 7):
    n = float(input((f'Digite o {c + 1}º número: ')))

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
print(f'Os números pares digitados foram: {lista[0]}')
print(f'Os números impares digitados foram: {lista[1]}')
