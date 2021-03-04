'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de
palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = input('Digite uma frase:').strip()
inverso = ''

for c in range(len(frase) - 1, -1, -1): #(caracteres totais - 1começa n o 0, -1 uma dps do 0, diminui 1)
    inverso += frase[c]
    #dps de capturar o valor da frase inversa iremos comparar
if frase == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
