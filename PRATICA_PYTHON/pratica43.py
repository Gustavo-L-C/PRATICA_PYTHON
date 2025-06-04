#03.06.25
#ESTRUTURAS DE REPETIÇÃO - 05

#FOR - 04
#PRATICA

matriz = [[1,2,3],[4,5,6],[7,8,9],[0]] # matriz

print('_________________________________________________________________________________________________________________')

for item in matriz[0]: # para cada item dentro da (item na posição 0)
    print(item) # imprimi item

print('_________________________________________________________________________________________________________________')

for linha in matriz: # para cada linha dentro de matriz
    print('---') # imprimi linha
    for coluna in linha: # para cada coluna dentro de linha
        print(coluna) # imprimi coluna
# utilizando um for dentro de outro