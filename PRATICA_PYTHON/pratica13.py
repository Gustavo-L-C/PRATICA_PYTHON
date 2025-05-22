#30.11.24
#UTILIZANDO MÓDULOS - 01#

from math import sqrt #importa uma funcionalidade especifica de um módulo
#import math #importa o módulo


n1 = int(input('Digite um numero:'))
r = sqrt(n1) #importando somente a função sqrt
#r = math.sqrt(n1) #importando o módulo completo

print(f'A raiz de {n1} é igual a {r:.2f}')