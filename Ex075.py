'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

nums = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
        int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))

cont = 0
vezes9 = 0


for cont in nums:       #Cont pegará os valores de nums e então poderei comparar com a máscar 9, ou seja, estou atribuindo a cont os valores de nums, 1 de cada vez.
    if cont == 9:
        cont += 1
        vezes9 += 1
    elif cont == 4:
        break

print(f'O número 9 apareceu {vezes9} vezes')    #Poderia ter feito somente nums.count(9)
if nums.count(3) > 0:
    print(f'O primeiro 3 foi digitado  na posição: {nums.index(3)}')
else:
    print('O número 3 não foi digitado')

print('Os valores pares são: ')
for n in nums:
    if n % 2 == 0:
        print(n,end=' ')
