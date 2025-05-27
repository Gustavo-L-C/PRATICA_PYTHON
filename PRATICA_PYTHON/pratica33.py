#26.05.25
#jogo da Adivinhação com random.randint.

from random import randint

def JA():
    print('Olá Bem-Vindo ao JOGO DA ADIVINHAÇÂO!!!\n__________________________________________________')
    nome = str(input('Qual seu nome jogador? '))
    print('__________________________________________________')
    print(f'Tente Adivinhar o número {nome} correto entre 1 e 20\n')

    n = randint(1, 20)

    t = 0
    p = 0

    while p != n:

        try:
            p = int(input(f'Qual seu palpite {nome}(entre 1 e 20)? '))
            t += 1

            if p < n:
                print(f'Tente um número maior {nome}.\n')
            elif p > n:
                print(f'Tente um número menor {nome}.\n')
            else:
                print(f'\nBoa {nome} você acertou o número {n} em {t} tentativas.\n')

        except ValueError:
            print('Número Inválido...')

    print(f'Obrigado por jogar {nome}!')
JA()