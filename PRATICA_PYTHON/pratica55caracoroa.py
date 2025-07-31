# CARA OU COROA - 23/07/2025

from random import randint

co = '👑'
ca = '😐'
mo = '🪙'

print(f'{ca} Cara ou Coroa {co}\n')

melhor = int(input('Quantas Vezes quer jogar: '))

print(' ')

op1 = input(f'{ca}- O que será Cara: ')
op2 = input(f'{co}- O que será Coroa: ')

for quantidade in range(melhor):

    cc = randint(1,2)

    if cc == 1:
        print(f'\nGirando {mo * 3}')
        print(f'{ca} Cara', op1)

    elif cc == 2:
        print(f'\nGirando {mo * 3}')
        print(f'{co} Coroa', op2)