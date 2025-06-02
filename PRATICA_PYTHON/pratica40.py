#02.06.25
# PRÁTICA

print('_________________________________________________________________________________________________________________')

v1 = float(input('1- Insira o valor do produto: R$ '))
v2 = float(input('2- Insira o valor do frete (caso seja grátis 0): R$ '))
# Lê dois valores

print('_________________________________________________________________________________________________________________')

if v2 in [0.0, 0]: # caso frete gratis
    frete = 'com frete grátis'
else: # se não
    frete = f'mais o frete de R$ {v2:.2f}'

dolar = 5.68 # valor do dolar data 02.06.2025
produto_frete = v1 + v2 # somamos o valor do produto mais o frete
real_dolar = produto_frete / dolar # convertemos o valor do produto mais frete para dólares

valores = [real_dolar]
# Os valores foram agrupados em uma lista

total_de_impostos = 0
# para o calculo do valor total dos impostos

for item in valores: # Para cada item dentro da lista de valores

    if item >= 50.01: # Se o valor do item for maior ou igual a USD 50.01 a taxa é de 60%
       taxa = 0.6

    elif item >= 3000: # Se o valor do item for maior ou igual a USD 3000 a taxa é de 60%
        taxa = 0.6

    else: # Se não for a taxa é de 20%
        taxa = 0.2

    imposto = item * taxa
    valor_completo = imposto + item

    print(f'\nO item de valor R$ {v1:.2f} {frete}, convertendo ao dólar hoje temos um total de USD {real_dolar:.2f}.')
    print(f'Então o seu produto deve ser taxado em {taxa * 100:.2f}% de seu valor.')
    print(f'Dando um total de USD {imposto:.2f} ou R$ {imposto * dolar:.2f} em impostos.')
    print(f'O valor do produto com os impostos de R$ {imposto * dolar:.2f} da um total de R$ {valor_completo * dolar:.2f}.')

    total_de_impostos += imposto

print(f'\nO total de impostos de todos os itens é de \033[31mR$ {total_de_impostos * dolar:.2f}\033[m')

print('_________________________________________________________________________________________________________________')