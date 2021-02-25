dist = float(input('Digite a distância q o carro percorreu em Km:'))
dias = float(input('Digite a quantidade de dias que ele foi alugado:'))
val = dias * 60 + dist * 0.15

print('O valor do aluguel é de R${:.2f}'.format(val))
