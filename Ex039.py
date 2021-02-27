''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
    alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
    também deverá mostrar o tempo que falta ou que passou do prazo. '''
from datetime import date
anodenascimento = int(input('Digite seu ano de nascimento:'))
anoatual = date.today().year

if anoatual - anodenascimento == 18:
    print('{} é seu ano de alistamento.'.format(anoatual))
elif anoatual - anodenascimento < 18:
    print('Faltam {} anos para seu alistamento.'.format(18 - (anoatual - anodenascimento)))
else:
    print('Já fazem {} anos que você se alistou'.format((anoatual - anodenascimento) - 18))