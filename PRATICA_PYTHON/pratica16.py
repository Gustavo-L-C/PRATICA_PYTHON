#02.12.24
#PRATICA - 02#

#Criar um programa que LEIA um número e faça o calculo da RAIZ QUADRADA e depois SOME o resultado da raiz por 5.

from math import sqrt

nome = str(input('Qual seu nome: '))
n0 = int(input(f'Olá {nome}!, digite um numero para o calculo: '))

r = sqrt(n0)

s = r + 5

print(f'...\n{nome} a raiz quadrada de {n0} é igual a {r:.2f} e somando com 5 o resultado é {s:.2f}')
