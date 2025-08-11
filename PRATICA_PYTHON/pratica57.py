#01.08.25
#🐲💀☠️🍀🎲

from random import randint
from time import sleep

Lista_Emoji = ['🐲', '💀', '🍀', '☠️', '🎲']

Num_Tentativas = 0

print(f'{Lista_Emoji[0]} Rolamento D20 D&D {Lista_Emoji[0]}\n')

Classe_Dificuldade = int(input('Qual é Classe de Dificuldade do momento: '))

Num_Rolamentos = int(input('Digite o Número de Rolamentos: '))

print(' ')

for carregamento_quantidade_rolamentos in range(Num_Rolamentos):

    if Num_Rolamentos <= 10:
        sleep(0.5)
        print(f'{Lista_Emoji[4]}', end='')

    elif Num_Rolamentos >= 50:
        sleep(0.12)
        print(f'{Lista_Emoji[4]}', end='')

    else:
        sleep(0.25)
        print(f'{Lista_Emoji[4]}', end='')

print('\n')

for quantidade_rolamentos in range(Num_Rolamentos):

    Rolamento_Dados = randint(1, 20)
    Num_Tentativas += 1

    if Rolamento_Dados >= Classe_Dificuldade:
        if Rolamento_Dados == 20:
            print(f'{Num_Tentativas}- {Rolamento_Dados} SUCESSO CRÍTICO {Lista_Emoji[2]*3}')
            sleep(0.4)

        else:
            print(f'{Num_Tentativas}- {Rolamento_Dados} SUCESSO {Lista_Emoji[0]*3}')
            sleep(0.4)

    elif Rolamento_Dados == 1:
        print(f'{Num_Tentativas}- {Rolamento_Dados} FALHA CRITICA {Lista_Emoji[3]*3}')
        sleep(0.4)

    else:
        print(f'{Num_Tentativas}- {Rolamento_Dados} FALHO {Lista_Emoji[1]*3}')
        sleep(0.4)