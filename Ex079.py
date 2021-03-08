'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.'''

lista = list()
while True:
    n = int(input('Digite o número: '))
    if n not in lista:
        lista.append(n)
        resposta = input('Você quer continuar? [S/N] ').upper().strip()[0]
    else:
        print('Valor duplicado, não adicionado.')
        resposta = input('Você quer continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
lista.sort()
print(f'Os números adicionados foram: {lista}')