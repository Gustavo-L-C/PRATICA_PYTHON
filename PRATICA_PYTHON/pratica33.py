#26.05.25
#jogo da Adivinhação com random.randint.

from random import randint

def JA():
    print('Olá Bem-Vindo ao JOGO DA ADIVINHAÇÂO!!!\n')
    print('Tente Adivinhar o número correto entre 1 e 20')

    n = randint(1, 20)

    t = 0
    p = 0

    while p != n:

        try:
            p = int(input('Qual seu palpite jogador(entre 1 e 20)? '))
            t += 1

            if p < n:
                print('Tente um número maior.')

            elif p > n:
                print('Tente um número menor.')

            else:
                print(f'Boa jogador você acertou o número {n} em {t} tentativas.')
        except ValueError:
            print('Número Inválido.')

    print('Obrigado por jogar!')
JA()