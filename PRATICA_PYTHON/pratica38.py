#01.06.25
#ESTRUTURAS DE REPETIÇÂO - 04


#FOR - 03

v1 = float(input("Insira o valor: R$ "))
v2 = float(input("Insira o valor: R$ "))
v3 = float(input("Insira o valor: R$ "))
# Lê três valores

valores = [v1, v2, v3] # Os valores foram agrupados em uma lsita

total_de_impostos = 0

for item in valores: # Para cada item/valor dentro da lista de valores

    if item >= 500: # Se o valor do item for maior ou igual a 500 a taxa é de 20%
       taxa = 0.2
    else: # Se não  a taxa é de 10%
        taxa = 0.1

    imposto = item * taxa
    # calculo do imposto que é o item multiplicado pela taxa

    valor_completo = imposto + item
    # calculo total do item + imposto

    print(f'\nO valor R${item:.2f}, recebeu um imposto de {taxa * 100:.0f}%, ficando R${valor_completo:.2f}')
    print(f'Sendo o valor do imposto R${imposto:.2f} + o valor do item R${item:.2f} = R${valor_completo:.2f}\n')

    total_de_impostos += imposto
    # calcular o total de imposto dos três itens isolados e somados


print(f'O total de imposto R${total_de_impostos:.2f}')