#26.05.25
#jogo da Adivinhação com random.randint.

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

    while p != n:
        print(f'\n Vamos começar {nome}!!')
        try:

            p = int(input(f'Qual seu palpite {nome}(entre 1 e 20)? '))
            t += 1

            if p < n:
                print(f'Tente um número maior {nome}.')
            elif p > n:
                print(f'Tente um número menor {nome}.')
            else:
                print(f'\nBoa {nome} você acertou o número {n} em {t} tentativas.\n')
                print(f'Tome seu prêmio {nome}.{premio}\n')

                ap = str(input('Quer abrir seu prêmio(S/N)? '))
                if ap == 'S':
                    print('\n⚔️⚔️Toma Elden Ring Night Rein⚔️⚔️')

                else:
                    print('\nOK.')

        except ValueError:
            print('Número Inválido...')

    print(f'Obrigado por jogar {nome}!')
JA()