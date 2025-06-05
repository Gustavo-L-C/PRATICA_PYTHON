#05.06.25

#MÃO LIVRE - 02

# gera senhas 3.0
# gerar senhas seguras/complexas
# gerar senhas numéricas simples
# utilizando randint, secrets, variáveis, if/elif/else e for

from random import randint # importando radint
import secrets # importando secrets
from bancodenomes import bancos_nomes # importando o banco de nomes "cadastrados"

numeracao = 0 # numeração na repetição

print('_________________________________________________________________________________________________________________') # só decoração

print('\n\033[34m--Gerador de senhas 3.0--\033[m\n') # titulo / só decoração

nome = str(input('Qual seu nome? ')) # recebe um nome

nomes = bancos_nomes # lista de nomes que possuem acesso para gerar senhas

print('_________________________________________________________________________________________________________________') # só decoração

#_________________________________________________________________________________________________________________if_nome_escolha
if nome in nomes: # se o nome recebido está dentro da lista de nomes

    print(f'\nSeja bem vindo {nome}!\n')  # será bem-vindo

    segura_simples = str(input('Que tipo de senha você precisa(\033[36msegura\033[m ou \033[35msimples\033[m)? ')) # pergunta se você precisa de uma senha segura ou simples

    #_________________________________________________________________________________________________________________if_senha_simples
    if segura_simples in ['simples', 'Simples', 'SIMPLES']: # para senhas simples

        se2 = int(input(f'\n{nome} escolha até que número sera usado para a senha (de 1 a \033[34msua escolha\033[m, sempre será partindo de 1): '))  # escolher o "range" numérico que será utilizado para a senha

        sr1 = 1  # número minimo
        sr2 = se2  # número maximo
        # senha range

        print(f'\nA senha será de {sr1} a {sr2}.\n')  # mostra o "range" numérico da senha

        quantidade = int(input('De quantos senhas precisará? ')) # pergunta a quantidade de senhas a serem geradas

        for numero in range(quantidade): # para cada número dentro do range(quantidade de repetições escolhidas na variável 'quantidade')

            numeracao += 1 # numeração para as repetições, só decoração

            se1 = randint(sr1, se2)
            se2 = randint(sr1, sr2)
            se3 = randint(sr1, se2)
            se4 = randint(sr1, sr2)
            se5 = randint(sr1, se2)
            se6 = randint(sr1, sr2)
            # número aleatorio dentro do "range" pré-estabelecido(em 'se2')

            senha = [se1, se2, se3, se4, se5, se6] # senha gerada de 6 números aleatórios para cada repetição

            print(f'\n{numeracao}- Sua senha simples: {senha}') # mostra a/as senhas geradas
    # _________________________________________________________________________________________________________________if_senha_simples

    #_________________________________________________________________________________________________________________elif_senha_segura
    elif segura_simples in ['segura', 'Segura', 'SEGURA']: # para senhas seguras

        tipo_senha = str(input('\nDigite o tipo de senha (\033[32multra\033[m, \033[33mmuito\033[m, \033[31mmédia\033[m): ')) # pergunta o tipo de senha segura, sendo elas, ultra segura, muito segura e de média segurança
       # quantidade = int(input(f'{nome}, quantas senhas precisará? ')) # pergunta a quantidade de senhas a serem geradas
       # caracteres = int(input(f'{nome}, quantos caracteres a senha precisa? ')) # pergunta a quantidade de caracteres que serão utilizados na senha
        print(' ') # pula linha

        # _________________________________________________________________________________________________________________if_senha_ultra
        if tipo_senha in ['ultra', 'Ultra', 'ULTRA']: # ultra segura

            quantidade = int(input(f'{nome}, quantas senhas precisará? '))  # pergunta a quantidade de senhas a serem geradas

            caracteres = int(input(f'{nome}, quantos caracteres a senha precisa? '))  # pergunta a quantidade de caracteres que serão utilizados na senha

            for numero in range(quantidade):  # para cada número dentro do range(quantidade de repetições escolhidas na variável 'quantidade')

                numeracao += 1  # numeração na repetição, só decoração

                print(f'{numeracao}- Sua senha segura de {tipo_senha} segurança:','\033[32m',secrets.token_bytes(caracteres),'\033[m') # mostra a/as senhas geradas
        # _________________________________________________________________________________________________________________if_senha_ultra

        # ___________________________________________________________________________________________________________________elif_senha_muito
        elif tipo_senha in ['muito', 'Muito', 'MUITO']: # muito segura

            quantidade = int(input(f'{nome}, quantas senhas precisará? '))  # pergunta a quantidade de senhas a serem geradas

            caracteres = int(input(f'{nome}, quantos caracteres a senha precisa? '))  # pergunta a quantidade de caracteres que serão utilizados na senha

            for numero in range(quantidade):  # para cada número dentro do range(quantidade de repetições escolhidas na variável 'quantidade')

                numeracao += 1  # numeração na repetição, só decoração

                print(f'{numeracao}- Sua senha segura de {tipo_senha} segurança:','\033[33m',secrets.token_urlsafe(caracteres),'\033[m') # mostra a/as senhas geradas
        # _________________________________________________________________________________________________________________elif_senha_muito

        # _________________________________________________________________________________________________________________elif_senha_media
        elif tipo_senha in ['média', 'media', 'Média', 'Media', 'MÉDIA', 'MEDIA']: # média segurança

            quantidade = int(input(f'{nome}, quantas senhas precisará? '))  # pergunta a quantidade de senhas a serem geradas

            caracteres = int(input(f'{nome}, quantos caracteres a senha precisa? '))  # pergunta a quantidade de caracteres que serão utilizados na senha

            for numero in range(quantidade): # para cada número dentro do range(quantidade de repetições escolhidas na variável 'quantidade')

                numeracao += 1 # numeração na repetição, só decoração

                print(f'{numeracao}- Sua senha segura de {tipo_senha} segurança:','\033[31m', secrets.token_hex(caracteres),'\033[m') # mostra a/as senhas geradas

        else:  # caso nome não esteja na lista

            uma_senha1 = '123456'  # para quem possui acesso

            print(f'\nSua senha : {uma_senha1}\n')  # mostra a senha fraca "gerada"
        # _________________________________________________________________________________________________________________elif_senha_media

    # _________________________________________________________________________________________________________________elif_senha_segura

    #_________________________________________________________________________________________________________________else_tipo_de_senha
    else: # caso nome não esteja na lista

        uma_senha2 = '123456' # para quem possui acesso

        print(f'Sua senha : {uma_senha2}') # mostra a senha fraca "gerada"
    #_________________________________________________________________________________________________________________else_tipo_de_senha

# _________________________________________________________________________________________________________________if_nome_escolha

#_________________________________________________________________________________________________________________else_nome
else:  # caso nome não esteja na lista

    uma_senha3 = '123456'  # para quem não possui acesso

    print(f'\nSua senha : {uma_senha3}')  # mostra a senha fraca "gerada"
#_________________________________________________________________________________________________________________else_nome

print(f'\nTchau {nome}!') # tchau

print('_________________________________________________________________________________________________________________') # só decoração

#OBS. quantidade de caracteres das senhas seguras estão "estranhas" dar uma olhada depois