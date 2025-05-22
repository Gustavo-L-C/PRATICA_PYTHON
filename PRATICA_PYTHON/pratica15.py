#01.12.24
#PRATICA - 01#

#Criar um programa que LEIA uma "sequência" de números (ex: 1, 100) e sorteie e MOSTRE um número ALEATÓRIO entre a "sequência"
#após isso o programa deve LER o nome de uma pessoa e MOSTRAR seu nome e numero

from random import randint

print(f'{"SORTEIO":*^19}\n')

n0 = int(input('Digite o numero inicial (ex: 1): '))
n1 = int(input('Digite o numero final (ex: 100): '))

s = randint(n0, n1)

print(f'O numero sorteado foi {s}\n')

p = str(input('\nDigite o nome do vencedor: '))

print(f'Parabens {p} do numero {s} voce ganhou um ...')

