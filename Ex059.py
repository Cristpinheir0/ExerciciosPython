'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:

    opcao = int(input(''
                      '[ 1 ] somar\n'
                      '[ 2 ] multiplicar\n'
                      '[ 3 ] maior\n'
                      '[ 4 ] novos números\n'
                      '[ 5 ] sair do programa\n'))
    if opcao == 1:
       print('{} + {} = {}.'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('{} x {} = {}.'.format(num1, num2, num1 * num2))
    elif opcao ==3:
        if num1 > num2:
            print('{} é maior do que {}.'.format(num1, num2))
        elif num2 > num1:
            print('{} é maior do que {}.'.format(num1, num2))
        else:
            print('Os dois número são iguais.')
    elif opcao == 4:
        num1 = float(input('Digite o novo primeiro número: '))
        num2 = float(input('Digite o noov segundo número: '))

    elif opcao == 5:
        print('Programa finalizado.')
    else:
        opcao = int(input('[ 1 ] somar\n'
                      '[ 2 ] multiplicar\n'
                      '[ 3 ] maior\n'
                      '[ 4 ] novos números\n'
                      '[ 5 ] sair do programa\n'))
opcao = 0
