'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
#           0  1   2
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
pares = 0
soma = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição {[l]},{[c]}: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        if l == 1 and maior < matriz[l][c]:
            maior = matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end=' ')
    print()
print(f'A soma de todos os valores pares digitados é = {pares}')
print(f'A soma dos valores da terceira coluna é = {soma}')
print(f'O maior valor da segunda linha é = {maior}')


