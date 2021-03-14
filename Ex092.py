'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

Para aposentadoria irei colocar idade com contribuição= 63 e 15 anos de contribuição
'''

from datetime import date

hj = date.today().year

cadastro = {}

cadastro['Nome'] = str(input('Nome: '))
cadastro['Ano de nascimento'] = int(input('Ano de nascimento: '))
cadastro['Idade'] = hj - cadastro['Ano de nascimento']
cadastro['Carteira de Trabalho'] = int(input('Carteira de Trabalho(0 não possui)'))

if cadastro['Carteira de Trabalho'] != 0:
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Tempo de contribuição'] = hj - cadastro['Ano de contratação']
    if cadastro['Tempo de contribuição'] < 15:
        cadastro['Tempo de contribuição necessária'] = 15 - cadastro['Tempo de contribuição']
    else:
        if cadastro['Idade'] < 63:
            cadastro['Idade necessária'] = 63 - cadastro['Idade']
            cadastro['Aposentadoria'] = 'Você não pode se aposentar'
        else:
            cadastro['Aposentadoria'] = 'Você pode se aposentar'

for k, v in cadastro.items():
    print(f'{k} = {v}')
