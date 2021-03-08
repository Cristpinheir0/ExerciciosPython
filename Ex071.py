''' Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
 a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

saque = int(input('Digite o valor a se sacado: '))
cedula = 50
totced = 0
while True:
    if saque >= cedula:
        saque -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} cédulas de R${cedula}]')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if saque == 0:
            break
