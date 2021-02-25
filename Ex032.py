#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#from datetime import date /biblioteca q pode pegar a data sem ter que atualizar o código
ano = int(input('Digite um ano para ver se ele é ou será bissexto:'))

if ano % 4 == 0:
    if ano > 2021:
        print('O {} será um ano bissexto.'.format(ano))
    elif ano == 2021:
        print('O {} é um ano bissexto'.format(ano))
    else:
        print('O {} foi um ano bissexto'.format(ano))
else:
    if ano >2021:
        print('O {} não será um ano bissexto'.format(ano))
    elif ano == 2021:
        print('O {} não é um ano bissexto'.format(ano))
    else:
        print('O {} não foi um ano bissexto'.format(ano))