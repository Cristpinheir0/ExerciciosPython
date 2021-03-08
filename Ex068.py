'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

vitorias = 0

while True:
    escolha = input('Par(P) ou Ímpar(I)?').strip().upper()[0]
    n = int(input('Escolha seu número: '))
    npc = randint(0, n)

    if escolha == 'P':    #Par para ganhar
        if n % 2 == 0:  #Par usuario
            if npc % 2 == 0:    #Par pc
                vitorias += 1
                print(f'Você ganhou {n} x {npc}.')
            else:   #Ímpar pc
                print(f'Você perdeu {n} x {npc}.')
                break
        else: #Ímpar usuario
            if npc % 2 == 0: #Par pc
                print(f'Você perdeu {n} x {npc}.')
                break
            else:   #Ímpar pc
                vitorias += 1
                print(f'Você ganhou {n} x {npc}.')

    else:   #escolha == 'I'
        if n % 2 == 0:  # Par usuario
            if npc % 2 == 0:  # Par pc
                print(f'Você perdeu {n} x {npc}.')
                break
            else:  # Ímpar pc
                vitorias += 1
                print(f'Você ganhou {n} x {npc}.')
        else:  # Ímpar usuario
            if npc % 2 == 0:  # Par pc
                vitorias += 1
                print(f'Você ganhou {n} x {npc}.')
            else:  # Ímpar pc
                print(f'Você perdeu {n} x {npc}.')
                break

print(f'Você ganhou {vitorias} partidas consecutivas')
#Assiti a resolução do ex e vi que a lógica de q (n + npc) % 2 == 0 if par = vitoria seria bem mais simples.