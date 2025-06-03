#02.06.25
#Atualizando

#gerador de senhas 2.0

from random import randint # importando o radint

repetir = 0 # numerção na repetição

print('_________________________________________________________________________________________________________________') # só decoração

print('\n\033[34m--Gerador de senhas--\033[m\n') # só decoração

nome = str(input('Qual seu nome? ')) # Recebe um nome

se2 = int(input(f'{nome} escolha até que número sera usado para a senha (de 1 a \033[34msua escolha\033[m, sempre será partindo de 1): ')) # escolher o "range" numerico que será utilizado para a senha

nomes = ['Gustavo', 'GUSTAVO', 'gustavo'] # lista de nomes que possuem acesso

print('_________________________________________________________________________________________________________________') # só decoração

s1 = 1 # numero minimo
s2 = se2 # numero maximo

print(f'A senha será de {s1} a {s2}.') # mostra o "range" numerico da senha

print('_________________________________________________________________________________________________________________') # só decoração

if nome in nomes: # se o nome recebido está dentro da lista de nomes
    print(f'\nSeja bem vindo {nome}!') # será bem vindo

    quantidade = int(input('De quantos senhas precisará? ')) # pergunta a quantidade de senhas a serem geradas

    for numero in range(quantidade): # para cada numero de repetições recebidas de quantidade

        repetir += 1 # numerção na repetição

        se1 = randint(s1, se2)
        se2 = randint(s1, s2)
        se3 = randint(s1, se2)
        se4 = randint(s1, s2)
        se5 = randint(s1, se2)
        se6 = randint(s1, s2)
        # numero aleatorio dentro do "range" pre estabelecido

        senha = [se1, se2, se3, se4, se5, se6] # senha gerada de 6 numeros aleatorios para cada repetição

        print(f'{repetir}- A senha do dia é: {senha}\n') # mostra a/as senhas geradas
        # print(f'{repetir}- A senha do dia é: {se1, se2, se3, se4, se5, se6}\n') # outro jeito de mostrar

else: # caso nome não esteja na lista
    print(f'\nTchau {nome}!') # tchau

print('_________________________________________________________________________________________________________________') # só decoração
