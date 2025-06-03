#26.05.25
#jogo da Adivinhação com random.randint.

from random import randint

import random

def JA(): # inicio da "janela"

    print('Olá Bem-Vindo ao JOGO DA ADIVINHAÇÂO!!!\n__________________________________________________')

    nome = str(input('Qual seu nome jogador? '))

    print('__________________________________________________')

    print(f'Tente Adivinhar o número {nome} correto entre 1 e 20\n')

    n = randint(1, 20) # numeração que de ser adivinhada de 1 a 20

    premio = '🎁' # premio

    t = 1 # numero de tentativas

    p = 0 # numero de palpites

    premio1 = ['Elden Ring Night Rein', 'Monster Hunter Wilds', 'Hell Divers', 'Space Marine 2'] # lista de premios

    print(f'\n Vamos começar {nome}!!') # start

    premiacao = random.choice(premio1) # pega um premio aleatório da lista de premios

    while p != n: # jogo acaba quando o palpite for igual ao numero aleatorio n

        try:

            p = int(input(f'{t}- Qual seu palpite {nome}(entre 1 e 20)? ')) # palpite do jogador

            t += 1 # contabilizando o numero de tentativas

            if p < n:
                print(f'\033[34mTente um número maior {nome}.\033[m') # quando o numero é menor

            elif p > n:
                print(f'\033[35mTente um número menor {nome}.\033[m') # quando o numero é maior

            else:
                print(f'\n\033[33mBoa {nome} você acertou o número \033[32m{n}\033[33m em \033[32m{t - 1}\033[33m tentativas.\n\033[m') # quando o numero é acertado

                print(f'Tome seu prêmio {nome}.{premio}\n') # premiação

                ap = str(input('Quer abrir seu prêmio(S/N)? ')) # para abrir o premio ou não

                if ap in ['S', 's', 'sim', 'Sim', 'SIM']: # recebe o premio aleatorio
                    print(f'\n⚔️⚔️Toma \033[34m{premiacao}\033[m⚔️⚔️')

                else:
                    print('\nOK.')

        except ValueError: 

            print('\033[31mNúmero Inválido..\033[m')

    print(f'Obrigado por jogar {nome}!')

JA() # fim da "janela"