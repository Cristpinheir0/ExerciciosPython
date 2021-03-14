'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.'''

lista = [int(input('Digite um número: '))]
pares = []
impares = []

r = input('Quer continuar? [S/N] ').upper().strip()[0]

while True:
    if r == 'S':
        lista.append(int(input('Digite um número: ')))
        r = input('Quer continuar? [S/N] ').upper().strip()[0]
    else:
        break
for c in lista:
    if c % 2 != 0:
        impares.append(c)
    else:
        pares.append(c)

print(f'A lista digitada foi: {lista}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números impares digitados foram: {impares}')