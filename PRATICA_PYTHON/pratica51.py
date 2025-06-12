#12.06.25
#FUNÇÕES - 04

# DEF - 04

# Calculador simples

# calculos

def soma(): # SOMA
    somar = s1 + s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {somar:.2f}') # imprimi o resultado

def subtracao(): # SUBTRAÇÃO
    subtrair = s1 - s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {subtrair:.2f}') # imprimi o resultado

def multiplicacao(): # MULTIPLICAÇÃO
    multiplicar = s1 * s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {multiplicar:.2f}') # imprimi o resultado

def divisao(): # DIVISÃO
    dividir = s1 / s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {dividir:.2f}') # imprimi o resultado

# calculos

s1 = float(input('Digite um numero: ')) # coleta o primeiro valor
s2 = float(input('Digite outro numero: ')) # coleta o segundo valor

esc = str(input('Qual tipo de calculo deseja executar? ')) # coleta o tipo de calculo

# listas facilitadoras
som = ['soma','Soma','SOMA'] # soma
sub = ['subtração','Subtração','SUBTRAÇÃO'] # subtração
mul = ['multiplicação','Multiplicação','MULTIPLICAÇÃO'] # multiplicação
div = ['divisão','Divisão','DIVISÃO'] # divisão

if esc in som: # se for soma
    soma()

if esc in sub: # se for subtração
    subtracao()

if esc in mul: # se for multiplicação
    multiplicacao()

if esc in div: # se for divisão
    divisao()

else: # para valores inválidos
    print('Invalido')



