'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import  date

anoatual = date.today().year
anodenascimento = int(input('Digite seu ano de nascimento:'))
idade = anoatual - anodenascimento

if idade <= 9:
    print('Você é da categoria MIRIM.')
elif idade <=14:
    print('Você é da categoria INFANTIL')
elif idade <=19:
    print('Você é da categoria JÚNIOR')
elif idade <= 25:
    print('Você é da categoria SÊNIOR')
else:
    print('Você é da categoria MASTER')