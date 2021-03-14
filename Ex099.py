'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def maior(* nums):
    c = m = 0
    print(f'\nAnalisando: ', end=' ', flush=True)
    for v in nums:
        print(v, end=' ')
        sleep(0.3)
        if c == 0:
            m = v
        else:
            if v > m:
                m = v
        c += 1
    sleep(0.3)
    print(f'\nO maior valor digitado foi: {m}')
    sleep(0.3)


maior(3, 9, 2, 3, 6)
maior(8, 3, 7, 2, 4, 99, 2312, 3223, 3563, 3)
maior(-2, 33, 32, 37, 3132, 3121231, 3213125, 63453)
