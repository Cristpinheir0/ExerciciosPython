'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

total = 0
cont = 0

for c in range(1,5):
    nome = input('Digite o nome da {}º pessoa: '.format(c))
    idade = int(input('Digite a idade da {}º pessoa: '.format(c)))
    sexo = int(input('Digite o sexo da {}º pessoa: \n(0) feminino:\n(1) masculino:'.format(c)))

    total += idade

    if sexo == 1:
        hvelho = idade
        nvelho = nome

        if hvelho < idade:
            hvelho = idade
            nvelho = nome
    elif sexo == 0:
        if idade < 20:
            cont += 1

print('A média da idade das pessoas é de {} anos'.format( total / 4))
print('O homem mais velho é o {} com {} anos'.format(nvelho, hvelho))
print('Existem {} mulheres com menos de 20 anos'.format(cont))
