#30.05.25
#ESTRUTURAS DE REPETIÇÂO - 01

from random import randint

#FOR - 01

l1 = 1
l2 = 100

for ran in range(10):

    ran = randint(l1, l2)

    if ran >= 90:
        print(f'sorteado {ran}')

    else:
        print(f'numero {ran}')

print('Acabou')