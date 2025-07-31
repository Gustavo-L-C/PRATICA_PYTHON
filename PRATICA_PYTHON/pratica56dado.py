# DADO - 31/07/2025

from random import randint
from time import sleep

#Receber o tipo de dado d6, d20, d100, ...
#Rolar o dado escolhido quantas vezes for decidido
#Receber quantas vezes o dado será lançado
#Por na tela os resultados do giro ou de cada giro do dado
#🎲

dd = '🎲'
ng = 0

print(f'{dd} Rolando os Dados {dd}\n')

tipo = int(input('Digite o tipo de dado (ex: digite 20 para dado D20): '))
print(f'Tipo de Dado escolhido: D{tipo}\n')

giros = int(input('Digite a quantidade de rolamentos: '))
print(' ')

for giro in range(giros):

    re = randint(1,tipo)
    ng += 1

    print(f'{dd}rolando o dado...{dd}')
    sleep(1.5)
    print(f'{ng}- Resultado: {re}')
    print(' ')