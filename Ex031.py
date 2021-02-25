'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
 Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

d = float(input('Digite a distância de sua viagem:'))

if d <= 200:
    print('O valor da passagem para a distância {:.2f}Km será de {:.2f}R$'.format(d, d * 0.5))
else:
    print('O valor da passagem para a distância {:.2f}Km será de {:.2f}R$'.format(d, d * 0.45))