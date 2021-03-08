'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu
programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

nums = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número de 0 a 20: '))
while True:
    if n < 0 or n > 20:
        n = int(input('Valor digitado inválido. Digite um número de 0 a 20:'))
    else:
        break
print(nums[n])

resp = input('Você quer que continue a contagem? [S/N] ').upper().strip()[0]

while True:
    if resp != 'S' and resp != 'N':
        resp = input('Resposta inválida. Você quer que continue a contagem? [S/N] ').upper().strip()[0]

    if resp == 'S':
        if n != 20:
            n += 1
            print(nums[n])

    elif resp == 'N':
        break

print('Sequencia terminada.')
