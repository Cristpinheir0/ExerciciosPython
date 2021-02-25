#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Digite o comprimento da primeira reta:'))
reta2 = float(input('Digite o comprimento da segunda reta:'))
reta3 = float(input('Digite o comprimento da terceira reta:'))

# Para que tres retas possam formar um triangulo é necessário q a soma de duas retas seja > do que a outra

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível formar um triângulo com estas três retas.')
else:
    print('Não é possível formar um triângulo com estas três retas.')
