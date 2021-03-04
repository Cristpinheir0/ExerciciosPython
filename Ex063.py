'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

n = int(input('Digite quantos termos deseja ver da sequencia de Fibonacci: '))

c = 3
t1 = 0
t2 = 1

print('{} -> {}'.format(t1, t2), end=' ->')

while c <= n:
    s = t1 + t2
    print(' {}'.format(s), end=' ->')
    t1 = t2
    t2 = s
    c += 1
print('Acabou!')
