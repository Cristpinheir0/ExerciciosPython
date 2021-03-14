'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
conteúdo da estrutura na tela.'''
boletim = {}
boletim['Nome'] = input('Digite o nome do aluno: ')
boletim['Média'] = int(input('Digite a média do aluno: '))

if boletim['Média'] >= 7:
    boletim['Situação'] = 'aprovado'
else:
    boletim['Situação'] = 'reprovado'

for k,v in boletim.items():
    print(f'{k} é igual a {v}')
