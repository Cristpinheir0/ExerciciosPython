#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint

escolhausu = int(input('Escolha uma das poções:\n'
                    '(1): Pedra.\n'
                    '(2): Papel.\n'
                    '(3): Tesoura.\n'))
escolhapc = randint(1, 3)

if escolhausu == 1:
    if escolhapc == 2:
        print('Você perdeu: Pedra x Papel')
    elif escolhapc == 1:
        print('Empatou: Pedra x Pedra')
    else:
        print('Você ganhou: Pedra x Tesoura')
elif escolhausu == 2:
    if escolhapc == 1:
        print('Você ganhou: Papel x Pedra')
    elif escolhapc == 2:
        print('Empatou: Papel x Papel')
    else:
        print('Você perdeu: Papel x Tesoura')
else:
    if escolhapc == 1:
        print('Você perdeu: Tesoura x Pedra')
    elif escolhapc == 2:
        print('Você ganhou: Tesoura x Papel')
    else:
        print('Empatou: Tesoura x Tesoura')
