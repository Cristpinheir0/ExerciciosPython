'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
 foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

v = float(input('Digite a velocidade do veiculo'))
if v > 80:
    print('Você foi multado por estar em uma velocidade acima de 80Km/h, sua multa será de: {:.2f}R$.'.format((v - 80)*7))
else:
    print('Você não foi multado.')