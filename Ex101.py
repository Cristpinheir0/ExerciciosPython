'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

from datetime import date

def voto(data):
    idade = 0
    hj = date.today().year
    idade = hj - data
    if 18 > idade >= 16 or idade >= 70:
        return print(f'Com {idade} anos: Voto opcional.')
    elif 18 <= idade < 70:
        return print(f'Com {idade} anos: Voto obrigatório.')
    else:
        return print(f'Com {idade} anos: Voto negado.')


voto(int(input('Digite seu ano de nascimento: ')))
