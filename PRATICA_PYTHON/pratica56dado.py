# DADO

from random import randint

# receba o tipo de dado d6, d20, d100, ...
# gire o dado escolhido quantas vezes for decidido
# receber quantas vezes o dado será lançado
# por na tela os resultados do giro ou de cada giro do dado


tipo = int(input("Digite o tipo de dado (ex: digite 20 para dado D20): "))

print(f"Tipo escolhido: D{tipo}")

giros = int(input('Digite a quantidade de giros: '))

ng = 0

for giro in range(giros):

    re = randint(1,tipo)
    ng += 1

    print(f'{ng}- Resultado: {re}')