'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

lista =  'lápis', 3.00, 'borracha', 2.50, 'corretivo', 4.30
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(lista[c],'=', end = ' ')
    else: print(f'R${lista[c]:.2f}')