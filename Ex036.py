'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
 do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
 será negado.'''

vi = float(input('Digite o valor do imóvel:')) #Valor do imóvel
vs = float(input('Digite o valor de seu salário:')) #Valor do salário
tp = float(input('Digite em quantos anos será feito o pagamento:')) #Tempo de pagamento

pm = vi / (tp * 12) #Prestação mensal
ce = (vs * 30) / 100 #Corte de empréstimo, ou seja, se maior de pm não será dado o empréstimo

print('A prestação será de R${:.2f}'.format(pm))

if pm > ce:
    print('O empréstimo foi negado')
else:
    print('O empréstimo foi aceito')