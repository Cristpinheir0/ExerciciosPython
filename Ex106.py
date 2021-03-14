"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai 
aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará."""

def ajuda(com):
    help(com)

coman = ''

while True:
    coman = input('Biblioteca ou função: ')
    if coman.upper() == 'FIM':
        break
    else:
        ajuda(coman)
