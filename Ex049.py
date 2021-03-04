''' Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

n = int(input('Número para pegar a tabuada:'))
print('Tabuada:')
for cont in range(1, 11):
    print(n,'x', cont, '=', n * cont)
