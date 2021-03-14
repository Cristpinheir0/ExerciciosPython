'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem correta.'''

exp = str(input('Digite sua expressão: '))
cont = []

for c in exp:
    if c == '(':
        cont.append(c)
    elif c == ')':
        cont.pop()
if len(cont) == 0:
    print(f'A expressão {exp} está com uma estrutura correta.')
else:
    print(f'A expressão {exp} está com uma estrutura incorreta.')