#31.07.25
# DADO

from random import randint
from time import sleep

#Receber o tipo de dado d6, d20, d100, ...
#Rolar o dado escolhido quantas vezes for decidido
#Receber quantas vezes o dado será lançado
#Por na tela os resultados do giro ou de cada giro do dado
#🎲

emoji_dado = '🎲'
num_jogadas = 0

print(f'{emoji_dado} Rolando os Dados {emoji_dado}\n')

tipo = int(input('Digite o tipo de dado (ex: digite 20 para dado D20): '))
print(f'Tipo de Dado escolhido: D{tipo}\n')

giros = int(input('Digite a quantidade de rolamentos: '))

print(' ')

# Métodos - Carregamento I

#for pontos in range(NR):

 #   if NR <= 10:
    #    sleep(0.5)
     #   print(f'{LE[4]}', end='')

  #  elif NR >= 50:
   #     sleep(0.12)
      #  print(f'{LE[4]}', end='')

    #else:
     #   sleep(0.25)
      #  print(f'{LE[4]}', end='')

# Métodos - Carregamento II

for pontos in range(giros<=10):
    for roll in range(giros):
        sleep(0.5)
        print(f'{emoji_dado}', end='')

for pontos in range(giros>=50):
    for roll in range(giros):
        sleep(0.12)
        print(f'{emoji_dado}', end='')

for pontos in range(giros>=100):
    for roll in range(giros):
        sleep(0.25)
        print(f'{emoji_dado}', end='')

print('\n')

for giro in range(giros):

    re = randint(1,tipo)
    num_jogadas += 1

    print(f'{ng}- Resultado: {re}')
    sleep(0.3)