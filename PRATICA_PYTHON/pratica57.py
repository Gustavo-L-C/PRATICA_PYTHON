#01.08.25

#Em D&D, o dado D20 é usado para determinar o sucesso ou fracasso de ações e ataques, com resultados críticos (20) e falhas críticas (1).

# Ao rolar um D20, um número entre 1 e 20 é obtido, e esse resultado, comparado com uma dificuldade (CD) definida pelo mestre, determina o resultado da ação.
#Resultados do D20 em D&D:

#1 (Falha Crítica):
#Geralmente resulta em uma falha catastrófica, com consequências negativas para o jogador.

#2 a 19:
#Estes resultados indicam um sucesso ou fracasso dependendo da CD (dificuldade) da ação. Se o resultado for igual ou superior à CD, a ação é bem-sucedida, caso contrário, falha.

#20 (Sucesso Crítico):
#Normalmente garante um sucesso automático e pode causar efeitos adicionais, como dano dobrado em ataques ou outras vantagens, de acordo com as regras do jogo.

#Como funciona:
#O mestre define a CD: Para cada ação, o mestre estabelece um número-alvo (CD) que o jogador deve igualar ou superar com o D20.
#O jogador rola o D20: O jogador lança o dado e obtém um resultado entre 1 e 20.
#Resultado: Se o resultado do D20 for igual ou superior à CD, a ação é bem-sucedida. Caso contrário, a ação falha.

#Exemplo:
#Se um jogador precisa escalar um muro e o mestre define uma CD 15, o jogador precisa tirar 15 ou mais no D20 para escalar com sucesso.
# Se tirar 1, é uma falha crítica, e se tirar 20, é um sucesso crítico, de acordo com as regras do jogo.

#CD significa Classe de Dificuldade

#🐲💀☠️🍀🎲

from random import randint
from time import sleep

LE = ['🐲', '💀', '🍀', '☠️', '🎲']

N = 0

print(f'{LE[0]} Rolamento D20 D&D {LE[0]}\n')

CD = int(input('Qual é Classe de Dificuldade do momento: '))

RO = int(input('Digite o numero de rolamentos: '))

print(' ')

for pontos in range(RO):

    if RO <= 10:
        sleep(0.5)
        print(f'{LE[4]}', end='')

    elif RO >= 50:
        sleep(0.12)
        print(f'{LE[4]}', end='')

    else:
        sleep(0.25)
        print(f'{LE[4]}', end='')

print('\n')

for rolamentos in range(RO):

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