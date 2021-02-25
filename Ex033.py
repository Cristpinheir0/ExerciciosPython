#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))
#Diferente de C que usa oplogic'&&' para colocar mais de uma condiçao dentro de um if em Python será usado 'and'
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 < n3:
        menor = n2
    else:
        menor = n3

elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 < n3:
        menor = n1
    else:
        menor = n3

elif n3 > n1 and n3 > n2:
    maior = n3
    if n1 < n2:
        menor = n1
    else:
        menor = n2

elif n1 == n2:
    if n1 > n3:
        maior = n1, n2
        menor = n3
    else:
        maior = n3
        menor = n1, n2

elif n1 == n3:
    if n1 > n2:
        maior = n1, n3
        menor = n2
    else:
        maior = n2
        menor = n1, n3

else:
    if n2 > n1:
        maior = n2, n3
        menor = n1
    else:
        maior = n1
        menor = n2, n3

print('O maior número digitado é o número {} e o menor é o {}'.format(maior, menor))
