#12.06.25
#FUNÇÔES - 03

# DEF - 03

quantos = int(input('Digite um número para a contagem regressiva:'))

def contagem_regressiva(numero):

    for i in range(numero, -1, -1):
        print(i)

contagem_regressiva(quantos)