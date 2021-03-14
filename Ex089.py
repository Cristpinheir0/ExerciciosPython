'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
 boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

aluno = []
boletim = []
al = 1
while True:
    aluno.append(al)#0
    aluno.append(input('Digite o nome do aluno: '))#1
    aluno.append(float(input('Digite a primeira nota do aluno: ')))#2
    aluno.append(float(input('Digite a segunda nota do aluno: ')))#3
    aluno.append(float(aluno[2] + aluno[3]) / 2)#4

    boletim.append(aluno[:])
    aluno.clear()

    r = input('Deseja continuar? [S/N] ').strip()[0]
    if r in 'Nn':
        break
    al += 1

for a in range(0, len(boletim)):
    print(f'{boletim[a][0]:<4}    Aluno: {boletim[a][1]:<10}          Média: {boletim[a][4]:>8}')
while True:
    r = input('Deseja ver individualmente algum aluno? [S/N] ').strip()[0]
    if r in 'Nn':
        break
    a = int(input('Qual aluno você deseja ver? '))
    a -= 1
    print(f'{boletim[a][0]}     Aluno: {boletim[a][1]}      Nota 1: {boletim[a][2]}     Nota 2: {boletim[a][3]}     Média: {boletim[a][4]}')
