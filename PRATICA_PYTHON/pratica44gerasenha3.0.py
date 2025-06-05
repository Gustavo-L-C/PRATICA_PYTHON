#05.06.25
#MÃO LIVRE - 02

# gera senhas 3.0
# gerar senhas seguras/complexas
# gerar senhas numéricas simples
# utilizando variáveis, if/elif/else, for

from random import randint
import secrets

#variáveis
numeracao = 0

print('_________________________________________________________________________________________________________________') # só decoração

print('\n\033[34m--Gerador de senhas 3.0--\033[m\n') # só decoração

nome = str(input('Qual seu nome? ')) # Recebe um nome

nomes = ['Gustavo', 'GUSTAVO', 'gustavo'] # lista de nomes que possuem acesso para gerar senhas

print('_________________________________________________________________________________________________________________') # só decoração
#_________________________________________________________________________________________________________________
if nome in nomes: # se o nome recebido está dentro da lista de nomes

    print(f'\nSeja bem vindo {nome}!\n')  # será bem-vindo

    questao = str(input('Que tipo de senha você precisa(segura ou simples)? '))
#_________________________________________________________________________________________________________________
    if questao in ['simples', 'Simples', 'SIMPLES']:

        se2 = int(input(f'\n{nome} escolha até que número sera usado para a senha (de 1 a \033[34msua escolha\033[m, sempre será partindo de 1): '))  # escolher o "range" numérico que será utilizado para a senha

        s1 = 1  # número minimo
        s2 = se2  # número maximo

        print(f'\nA senha será de {s1} a {s2}.\n')  # mostra o "range" numérico da senha

        quantidade = int(input('De quantos senhas precisará? ')) # pergunta a quantidade de senhas a serem geradas

        for numero in range(quantidade): # para cada número dentro do range(quantidade de repetições escolhidas na variável 'quantidade')

            numeracao += 1 # numeração na repetição, só decoração

            se1 = randint(s1, se2)
            se2 = randint(s1, s2)
            se3 = randint(s1, se2)
            se4 = randint(s1, s2)
            se5 = randint(s1, se2)
            se6 = randint(s1, s2)
            # número aleatorio dentro do "range" pre estabelecido(em 'se2')

            senha = [se1, se2, se3, se4, se5, se6] # senha gerada de 6 números aleatórios para cada repetição

            print(f'\n{numeracao}- A senha do dia é: {senha}') # mostra a/as senhas geradas
#_________________________________________________________________________________________________________________
    elif questao in ['segura', 'Segura', 'SEGURA']:

        tipo_senha = str(input('\nDigite o tipo de senha (ultra, muito, média): ')) # pergunta o tipo de senha ultra segura, muito segura e de média segurança
        quantidade = int(input(f'{nome}, quantas senhas precisará? '))  # pergunta a quantidade de senhas a serem geradas
        caracteres = int(input(f'{nome}, quantos caracteres a senha precisa? ')) # pergunta a quantidade de caracteres que serão utilizados na senha
        print(' ')

        if tipo_senha in ['ultra', 'Ultra', 'ULTRA']:

            for numero in range(quantidade):  # para cada número dentro do range(quantidade de repetições escolhidas na variável 'quantidade')

                numeracao += 1  # numeração na repetição, só decoração

                print(f'{numeracao}- Sua senha segura {tipo_senha} segura:',secrets.token_bytes(caracteres))

        elif tipo_senha in ['muto', 'Muito', 'MUITO']:

            for numero in range(quantidade):  # para cada número dentro do range(quantidade de repetições escolhidas na variável 'quantidade')

                numeracao += 1  # numeração na repetição, só decoração

                print(f'{numeracao}- Sua senha segura {tipo_senha} segura:',secrets.token_urlsafe(caracteres))
        else:

            for numero in range(quantidade):

                numeracao += 1

                print(f'{numeracao}- Sua senha segura {tipo_senha} segura:',secrets.token_hex(caracteres))
#_________________________________________________________________________________________________________________
    else: # caso nome não esteja na lista
        uma_senha1 = '123456' # para quem não possui acesso
        print(f'\nSua senha : {uma_senha1}\nTchau {nome}!') # tchau
#_________________________________________________________________________________________________________________
else:  # caso nome não esteja na lista
    uma_senha2 = '123456'  # para quem não possui acesso
    print(f'\nSua senha : {uma_senha2}\nTchau {nome}!')  # tchau
#_________________________________________________________________________________________________________________

print(f'\nTchau {nome}!')

print('_________________________________________________________________________________________________________________') # só decoração