#02.06.25
#Atualizando

#gerador de senhas 2.0

from random import randint

s1 = 1
s2 = 60

se1 = randint(s1, s2)
se2 = randint(s1, s2)
se3 = randint(s1, s2)
se4 = randint(s1, s2)
se5 = randint(s1, s2)
se6 = randint(s1, s2)

senha = [se1, se2, se3, se4, se5, se6]

print('_________________________________________________________________________________________________________________')

print('\n\033[34m--Gerador de senhas--\033[m\n')
nome = str(input('Qual seu nome? '))
quantidade = int(input('De quantos senhas precisará? '))

print('_________________________________________________________________________________________________________________')

repetir = 0

nomes = ['Gustavo', 'GUSTAVO', 'gustavo']

for numero in range(quantidade):

    repetir += 1
    print(f'\nSeja bem vindo {nome}!')

    if nome in nomes:
        print(f'{repetir}- A senha do dia é: {senha}\n')

    else:
        print('Tchau!')

print('_________________________________________________________________________________________________________________')
