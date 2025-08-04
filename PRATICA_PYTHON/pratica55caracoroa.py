#23.07.25
# CARA OU COROA

from random import randint
from time import sleep

LE = ['👑', '😐', '🪙']


print(f'{LE[1]} Cara ou Coroa {LE[0]}\n')

melhor = int(input('Quantas Vezes quer jogar: '))

print(' ')

op1 = input(f'{LE[1]}- O que será Cara: ')
op2 = input(f'{LE[0]}- O que será Coroa: ')

print(' ')

for pontos in range(melhor):

    if melhor <= 10:
        sleep(0.5)
        print(f'{LE[2]}', end='')

    elif melhor >= 50:
        sleep(0.12)
        print(f'{LE[2]}', end='')

    else:
        sleep(0.25)
        print(f'{LE[2]}', end='')

print('\n')

for quantidade in range(melhor):

    cc = randint(1,2)

    if cc == 1:
        print(f'{LE[1]} Cara', op1)
        sleep(0.25)

    elif cc == 2:
        print(f'{co} Coroa', op2)
        sleep(0.25)