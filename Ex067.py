'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

n = int(input('Digite o número que deseja a tabuada: '))
c = 0
while True:
    if n < 0:
        break
    else:
        while c <= 10:
            print(f'{n} x {c} = {n * c}')
            c += 1


print('Programa de tabuada encerrado.')