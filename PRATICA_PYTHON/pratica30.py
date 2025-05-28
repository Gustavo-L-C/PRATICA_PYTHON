#20.05.25
#PRATICA - 11#

from random import randint

l1 = 1
l2 = 1000000

rl = randint(l1, l2)



if rl >= 900000:
    print(f'\nnúmero sorteado {rl}\n')

else:
    print(f'\ntoma seu número {rl}\n')
