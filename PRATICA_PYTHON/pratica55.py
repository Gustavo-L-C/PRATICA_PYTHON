# CARA OU COROA
from random import randint



print('😐 Cara ou Coroa 👑\n')

melhor = int(input('Quantas Vezes quer jogar: '))

print(' ')

op1 = input('😐- O que será Cara: ')
op2 = input('👑- O que será Coroa: ')

for quantidade in range(melhor):

    cc = randint(1,2)

    if cc == 1:
        print('\nGirando 🪙🪙🪙')
        print('😐 Cara', op1)

    elif cc == 2:
        print('\nGirando 🪙🪙🪙')
        print('👑 Coroa', op2)