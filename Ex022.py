""" Crie um programa que leia o nome completo de uma pessoa e mostre:
    – O nome com todas as letras maiúsculas e minúsculas.
    – Quantas letras ao todo (sem considerar espaços).
    – Quantas letras tem o primeiro nome."""

nome = input('Digite seu nome completo:').strip()#<- Importante para que espaços desnecessarios sejam "excluidos"
print('SEU NOME COM TODAS AS LETRAS MAIUSCULAS: {}'.format(nome.upper()))
print('seu nome com todas as letras minusculas: {}'.format(nome.lower()))

totaldecarac = (len(nome)) - (nome.count(' '))
print('A quantidade de caracteres na string sem os espaços é de: {}'.format(totaldecarac))

caracprimeira = len(nome.split()[0])
print('Seu primeiro nome tem {} caracteres'.format(caracprimeira))