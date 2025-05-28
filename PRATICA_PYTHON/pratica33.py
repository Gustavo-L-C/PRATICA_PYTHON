#26.05.25
#jogo da Adivinhação com random.randint.
import random
from random import randint

def JA():
    print('Olá Bem-Vindo ao JOGO DA ADIVINHAÇÂO!!!\n__________________________________________________')
    nome = str(input('Qual seu nome jogador? '))
    print('__________________________________________________')
    print(f'Tente Adivinhar o número {nome} correto entre 1 e 20\n')

    n = randint(1, 20)

    premio = '🎁'
    t = 0
    p = 0
    print(f'\n Vamos começar {nome}!!')


    while p != n:

        try:

            p = int(input(f'Qual seu palpite {nome}(entre 1 e 20)? '))
            t += 1


            if p < n:
                print(f'\033[34mTente um número maior {nome}.\033[m')

            elif p > n:
                print(f'\033[35mTente um número menor {nome}.\033[m')

            else:
                print(f'\n\033[33mBoa {nome} você acertou o número \033[32m{n}\033[33m em \033[32m{t}\033[33m tentativas.\n\033[m')
                print(f'Tome seu prêmio {nome}.{premio}\n')

                ap = str(input('Quer abrir seu prêmio(S/N)? '))
                if ap == 'S' or 's':
                    print('\n⚔️⚔️Toma \033[34mElden Ring Night Rein\033[m⚔️⚔️')
                else:
                    print('\nOK.')


        except ValueError:
            print('\033[31mNúmero Inválido..\033[m')

    print(f'Obrigado por jogar {nome}!')
JA()