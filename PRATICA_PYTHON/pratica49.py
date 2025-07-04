#11.06.25
#Atualizando

#gerador de senhas 2.0

from random import randint # importando radint
from bancodenomes import bancos_nomes # importando o banco de nomes "cadastrados"

def gerar_senha():

    print('\n\033[34m--Gerador de senhas--\033[m\n')  # só decoração

    nome = str(input('Qual seu nome? '))  # Recebe um nome

    se2 = int(input(
        f'{nome} escolha até que número sera usado para a senha (de 1 a \033[34msua escolha\033[m, sempre será partindo de 1): '))  # escolher o "range" numérico que será utilizado para a senha


    print('_________________________________________________________________________________________________________________')  # só decoração

    s1 = 1  # número minimo
    s2 = se2  # número maximo

    print(f'A senha será de {s1} a {s2}.')  # mostra o "range" numérico da senha

    print('_________________________________________________________________________________________________________________')  # só decoração

    repetir = 0  # numeração na repetição

    if nome in bancos_nomes: # se o nome recebido está dentro da lista de nomes

        print(f'\nSeja bem vindo {nome}!') # será bem-vindo

        quantidade = int(input('De quantos senhas precisará? ')) # pergunta a quantidade de senhas a serem geradas

        for numero in range(quantidade): # para cada número dentro do range(quantidade de repetições escolhidas na variável 'quantidade')

            repetir += 1 # numeração na repetição, só decoração

            se1 = randint(s1, se2)
            se2 = randint(s1, s2)
            se3 = randint(s1, se2)
            se4 = randint(s1, s2)
            se5 = randint(s1, se2)
            se6 = randint(s1, s2)
            # número aleatorio dentro do "range" pre estabelecido(em 'se2')

            senha = [se1, se2, se3, se4, se5, se6] # senha gerada de 6 números aleatórios para cada repetição

            print(f'{repetir}- A senha do dia é: {senha}\n') # mostra a/as senhas geradas
            # print(f'{repetir}- A senha do dia é: {se1, se2, se3, se4, se5, se6}\n') # outro jeito de mostrar a/as senha/as geradas

            print(f'\nTchau {nome}!')

    else: # caso nome não esteja na lista
        uma_senha = '123456' # para quem não possui acesso
        print(f'\nSua senha : {uma_senha}\nTchau {nome}!') # tchau

    return gerar_senha()

gerador_de_senhas = gerar_senha()

print('_________________________________________________________________________________________________________________') # só decoração
