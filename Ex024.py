#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite o nome da cidade:').strip().upper()

nome1 = cidade.split()[0]
print(nome1)

print('A cidade começa com a palavra "SANTO"? {}'.format('SANTO' in nome1))
