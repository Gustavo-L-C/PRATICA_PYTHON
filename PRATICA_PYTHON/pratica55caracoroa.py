#23.07.25
# CARA OU COROA

from random import randint
from time import sleep

co = '👑'
ca = '😐'
mo = '🪙'

print(f'{ca} Cara ou Coroa {co}\n')

melhor = int(input('Quantas Vezes quer jogar: '))

print(' ')

op1 = input(f'{ca}- O que será Cara: ')
op2 = input(f'{co}- O que será Coroa: ')

print(' ')


for pontos in range(melhor):

    if melhor <= 10:
        sleep(0.5)
        print(f'{mo}', end='')

    elif melhor >= 50:
        sleep(0.12)
        print(f'{mo}', end='')

    else:
        sleep(0.25)
        print(f'{mo}', end='')

print(' ')

for quantidade in range(melhor):

    cc = randint(1,2)

    if cc == 1:
        print(f'{ca} Cara', op1)
        

    elif cc == 2:
        print(f'{co} Coroa', op2)