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
# coletamos as notas

turma = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
# agrupamos as notas

def media_turma(turma): # definimos a média da turma

    qtd = len(turma) # pegamos a quantidade de alunos
    soma_notas = 0 # para a soma

    for notas in turma: # para cada nota na turma
        soma_notas += notas # somando as notas

    media_notas = soma_notas / qtd # calculando a média
    return media_notas

media_da_turma = media_turma(turma)
print(f'A média de nota da turma é {media_da_turma:.1f}') # mostrando a média

if media_da_turma >= 7: # se a média da turma for igual ou maior que 7
    print('Turma excelente') # Turma excelente
    maior_valor = max(turma) # pegamos a maior nota
    print(f'E a maior nota da turma foi {maior_valor:.1f}') # A maior nota

else: # se não
    print('Turma abaixo da média') # Turma abaixo da média
    maior_valor = max(turma) # pegamos a maior nota
    print(f'Sendo a maior nota da turma {maior_valor:.1f}') # A maior nota

# extra se a turma tem uma média de 7 o maior Turma excelente se não Turma abaixo da média
# extra exibi a maior nota da turma