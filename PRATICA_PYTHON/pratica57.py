#01.08.25
#🐲💀☠️🍀🎲

from random import randint
from time import sleep

LE = ['🐲', '💀', '🍀', '☠️', '🎲']

N = 0

print(f'{LE[0]} Rolamento D20 D&D {LE[0]}\n')

CD = int(input('Qual é Classe de Dificuldade do momento: '))

NR = int(input('Digite o Número de Rolamentos: '))

print(' ')

for pontos in range(NR):

    if NR <= 10:
        sleep(0.5)
        print(f'{LE[4]}', end='')

    elif NR >= 50:
        sleep(0.12)
        print(f'{LE[4]}', end='')

    else:
        sleep(0.25)
        print(f'{LE[4]}', end='')

print('\n')

for rolamentos in range(NR):

    RDD = randint(1, 20)
    N += 1

    if RDD >= CD:
        if RDD == 20:
            print(f'{N}- {RDD} SUCESSO CRÍTICO {LE[2]*3}')
            sleep(0.4)

        else:
            print(f'{N}- {RDD} SUCESSO {LE[0]*3}')
            sleep(0.4)

    elif RDD == 1:
        print(f'{N}- {RDD} FALHA CRITICA {LE[3]*3}')
        sleep(0.4)

    else:
        print(f'{N}- {RDD} FALHO {LE[1]*3}')
        sleep(0.4)