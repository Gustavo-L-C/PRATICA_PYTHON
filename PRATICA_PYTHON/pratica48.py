#09.06.25
#FUNÇÕES - 02

#DEF - 02

# Média da Turma
# coletar a nota de uma turma de 10 alunos
# e dar a média de nota da turma


n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))
n5 = float(input('Digite a nota 5: '))
n6 = float(input('Digite a nota 6: '))
n7 = float(input('Digite a nota 7: '))
n8 = float(input('Digite a nota 8: '))
n9 = float(input('Digite a nota 9: '))
n10 = float(input('Digite a nota 10: '))

turma = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

def media_turma(turma):

    qtd = len(turma)
    soma_notas = 0

    for notas in turma:
        soma_notas += notas
    media_notas = soma_notas/qtd
    return media_notas

media_da_turma = media_turma(turma)
print(f'A média de nota da turma é {media_da_turma}')
