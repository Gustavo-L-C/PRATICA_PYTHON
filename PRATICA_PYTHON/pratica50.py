#12.06.25
#FUNÇÕES - 03

# DEF - 03

quantos = int(input('Digite um número para a contagem regressiva: ')) # coleta o numero para a contagem "regressiva"

def contagem_regressiva(numero): # função contagem regressiva recebe um numero

    for i in range(numero, -1, -1): # para cada item no "range" de numero, -1 numero, -1 numero
        print(i) # imprimi item

contagem_regressiva(quantos) # recebe o numero da contagem "regressiva"