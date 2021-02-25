''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Digite o valo do salário:'))

if salario > 1250.00:
    print('O seu novo salário será de: {} com o aumento total de: {}'.format((salario * 10 / 100) + salario, (salario * 10) /100))
else:
    print('O seu novo salário será de: {} com o aumento total de: {}'.format((salario * 15 / 100) + salario, (salario * 15) /100))
