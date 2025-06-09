#09.08.25
#FUNÇÕES - 00

from bancodenomes import bancos_nomes

# DEF - 00

# def nome_da_função(parametro): # abrir
    # instruções
# nome_da_função(): # fechar

# definir função parametro
 # instruções da função
# ponto final

def hello(): # abrir

    print("Hello")

hello() # fechar

def calculo():

    valor = 2
    valor1 = valor * 2
    print(valor1)

calculo()

def nome_G():

    nome = str(input("Digite seu nome: "))

    if nome in bancos_nomes:

        print(f'Olá {nome}')
    else:
        print(f'Adeus {nome}')

nome_G()