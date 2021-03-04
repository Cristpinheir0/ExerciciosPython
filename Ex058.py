''' Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

tentativa = int(input('Tente acertar o valor sorteado de 0 a 10: '))
num = randint(0,10)

while tentativa != num:
    tentativa = int(input('Você não acertou, tente novamente: '))

print('Você acertou!!!')