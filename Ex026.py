"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
aparece a primeira vez e em que posição ela aparece a última vez."""

frase = input('Digite uma frase:').strip().upper()
print('A frase digitada possui {} caracteres "A", o primeiro "A" aparece na posição {} e aparece pela última vez em {}.'.format(frase.count('A'), frase.find('A') + 1, frase.rfind('A')+1))
