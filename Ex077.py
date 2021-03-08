'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.'''

tupla = 'carro', 'moto', 'bicicleta', 'casa', 'sapo', 'ferrari', 'feijão', 'agua'

for palavras in tupla:
    print(f'\nA palavra {palavras.upper()} tem as vogais: ',end='')
    for letras in palavras:
        if letras in 'aeiou':
            print(f'{letras}', end = ' ')