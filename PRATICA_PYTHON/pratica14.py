#30.11.24
#UTILIZANDO MÓDULOS - 02#

#import random
from random import randint

print(f'{"FAÇA O SEU SORTEIO":-^20}\n')


s1 = int(input('Digite o numero inicial (ex: 1):'))
s2 = int(input('Digite o numero final (ex: 100):'))

n = randint(s1, s2)


print(f'\nO numero sorteado foi {n}')