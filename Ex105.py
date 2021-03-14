'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''


def notas(*notas, situação=False):
    """
    função para calcular dados de turma de estudantes.
    :param notas: dos alunos
    :param situação: ver se a media da turma esta boa
    :return: dicionario com todas ifos
    """

    r = {'quantidade de notas': len(notas), 'maior nota': max(notas), 'menor nota': min(notas),
         'média da turma': sum(notas) / len(notas)}
    if situação:
        if r['média da turma'] >= 7:
            r['situação'] = 'Boa'
        elif r['média da turma'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Péssima'
    return r


resp = notas(6, 3, 5, 7, situação=True)
print(resp)

