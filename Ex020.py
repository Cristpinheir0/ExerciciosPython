import random

alunos = [0, 1, 2, 3]  # Poderia ter pego o alunos e ter embaralhado shuffle, random.shuffle(alunos), criando uma ordem

alunos[0] = input('Nome do primeiro aluno:')
alunos[1] = input('Nome do segundo aluno:')
alunos[2] = input('Nome do terceiro aluno:')
alunos[3] = input('Nome do quarto aluno:')

sequencia = random.sample(alunos, 4)
print('A sequencia das apresentações será: {}'.format(sequencia))
