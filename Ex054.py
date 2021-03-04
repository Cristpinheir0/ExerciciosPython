'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
 maioridade e quantas já são maiores.'''

contma = 0
contme = 0

for c in range(0,7):
    idade = int(input('Digite a idade da {}º pessoa:'.format(c + 1)))
    if idade >= 18:
        contma += 1
    else:
        contme += 1
print('Já atingiram a maioridade {} pessoas e não atingiram {} pessoas'.format(contma, contme))