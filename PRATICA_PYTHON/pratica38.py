#01.06.25
#ESTRUTURAS DE REPETIÇÂO - 04


#FOR - 03
#MÃO LIVRE

print('_________________________________________________________________________________________________________________')

v1 = float(input("1- Insira o valor: R$ "))
v2 = float(input("2- Insira o valor: R$ "))
v3 = float(input("3- Insira o valor: R$ "))
# Lê três valores

print('_________________________________________________________________________________________________________________')
print('\033[32mValor do Item\033[m / \033[33mTaxa\033[m / \033[34mValor Total\033[m / \033[31mImposto\033[m') # Só para organizar os valores
valores = [v1, v2, v3] # Os valores foram agrupados em uma lista

total_de_impostos = 0 # para o calculo do valor total dos impostos
n = 0 # Adicionado uma numeração para cada repetição

for item in valores: # Para cada item dentro da lista de valores

    if item >= 1000: # Se o valor do item for maior ou igual a 1000 a taxa é de 50%
       taxa = 0.5

    elif item >= 500: # Se o valor do item for maior ou igual a 500 a taxa é de 20%
        taxa = 0.2

    else: # Se não  a taxa é de 10%
        taxa = 0.1

    imposto = item * taxa
    # Calculo do imposto que é o item multiplicado pela taxa

    valor_completo = imposto + item
    # Calculo total do item + imposto

    n += 1
    # Adicionado uma numeração para cada repetição

    print(f'\n{n}- O item no valor de \033[32mR${item:.2f}\033[m, recebeu uma taxa de \033[33m{taxa * 100:.0f}%\033[m, ficando \033[34mR${valor_completo:.2f}\033[m')
    print(f'Sendo o valor do item \033[32mR${item:.2f}\033[m + o valor do imposto \033[31mR${imposto:.2f}\033[m = \033[34mR${valor_completo:.2f}\033[m')
    # Imprimindo o resultado do calculo de impostos, valor da taxa e o valor total do item mais impostos

    total_de_impostos += imposto
    # Calcular o total de imposto dos três itens isolados e somados


print(f'\nO total de impostos de todos os itens é de \033[31mR${total_de_impostos:.2f}\033[m')
# Imprimindo o valor total, exclusivamente, dos impostos
print('_________________________________________________________________________________________________________________')