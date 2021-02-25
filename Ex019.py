import random
alunos = [0, 1, 2, 3]

alunos[0] = input('Digite o nome do primeiro aluno:')
alunos[1] = input('Digite o nome do segundo aluno:')
alunos[2] = input('Digite o nome do terceiro aluno:')
alunos[3] = input('Digite o nome do quarto aluno:')

escolhido = random.randint(0, 3)#Poderia ser usado random.choice(alunos), escolhendo um dos alunos

print('O número sorteado foi o número: {}'.format(escolhido+1))
print('O aluno que irá limpar será o(a): {}'.format(alunos[escolhido]))
