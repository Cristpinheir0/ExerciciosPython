'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
digitação novamente até ter um valor correto.'''

sexo = input('Digite o sexo da pessoa M ou F: ').upper().strip()[0]
while sexo not in'MF':
    sexo = input('Escrita errada. Digite M para masculino ou F para feminino:').upper().strip()[0]
print('Sexo registrado com sucesso')