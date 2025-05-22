#03.12.24
#PRATICA -03#

#Criar um programa que LEIA três nomes e SORTEIE um deles de uma LISTA para saber quem que vai pagar a conta

from random import choice

print(f'\n{"QUEM QUE VAI PAGAR A CONTA?":-^40}\n')

n1 = str(input('Digte um nome:'))
n2 = str(input('Digite um nome:'))
n3 = str(input('Digite um nome:'))

l = [n1, n2, n3]

p = choice(l)

print(f'\nO sortudo da vez foi {p}')
