'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = []
pessoa = {}
media = 0
cont = 0
mulheres = []
acima = []
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    dados.append(pessoa.copy())
    pessoa.clear()
    if r == 'N':
        break
print(f'Foram cadastradas {len(dados)} pessoas.')
for p in dados:
    media += p['Idade']
    if p['Sexo'] == 'F':
        mulheres.append(p['Nome'])
    if p['Idade'] > media/3:
        acima.append(p['Nome'])

print(f'A média de idade das pessoas cadastradas é de: {media/3:.2f}')

print(f'As mulheres cadastradas foram:')
for c in mulheres:
    print(c)

print(f'\nAs pessoas acima da idade média são:')
for d in acima:
    print(d)


