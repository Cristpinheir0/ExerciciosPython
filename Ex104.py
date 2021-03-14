'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''


def leiaInt(m):
    while True:
        v = input(m)
        if v.isnumeric():
            break
        else:
            print('Resposta inválida.',end=' ')
    return v


v = leiaInt('Digite um número: ')
print(f'Você digitou o número {v}')
