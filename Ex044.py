'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''

valor = float(input('Digite o valor do produto:'))
condpag = int(input('Em qual forma de pagamento será feita a compra:\n'
                    '(1): À vista dinheiro / cheque 10% de desconto.\n'
                    '(2): À vista no cartão 5% de desconto.\n'
                    '(3): Em até 2x no cartão = preço normal.\n'
                    '(4): 3x ou mais no cartão 20% de juros.\n'))

if condpag < 1 or condpag > 4:
    condpag = int(input('Digite novamente conforme as opções:'))
elif condpag == 1:
    print('O valor do pagamento será de: {:.2f}R$'.format(valor * 0.9))
elif condpag == 2:
    print('O valor do pagamento será de: {:.2f}R$'.format(valor * 0.95))
elif condpag == 3:
    print('O valor do pagamento será de: {:.2f}R$'.format(valor))
else:
    print('O valor do pagamento será de: {:.2f}R$'.format(valor * 1.2))