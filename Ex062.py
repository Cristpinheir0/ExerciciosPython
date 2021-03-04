'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
ele disser que quer mostrar 0 termos.'''

a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        an = a1 + c * r
        print('O {}º termo da PA é = {}'.format(c, an))
        c += 1
    mais = int(input('Digite quantos termos a mais vc quer q mostre: '))
print('Programa finalizado')

