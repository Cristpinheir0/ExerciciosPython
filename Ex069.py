"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos."""

conti = 0   #Contador de maiores de 18 anos
conth = 0   #Contador de homens cadastrados
contm = 0   #Contador de mulheres com menos de 20 anos

while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa [F/M]: ').upper().strip()[0]
    continuar= input('Você quer continuar? [S/N]: ').strip().upper()[0]

    if idade > 18:
            conti += 1
    if sexo == 'M':
            conth += 1
    if sexo == 'F' and idade < 20:
            contm += 1
    if continuar == 'S':
        print('')
    elif continuar == 'N':
        break
    else:
        while continuar != 'SN':
            continuar = input('Você quer continuar? [S/N]: ').strip().upper()[0]
            if continuar == 'S' or continuar == 'N':
                break
print(f'{conti} pessoas tem mais de 18 anos, {conth} homens foram cadastrados e {contm} mulheres tem menos de 20 anos.')
