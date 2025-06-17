#12.06.25
#FUNÇÕES - 04

# DEF - 04

# Calculador simples

# listas facilitadoras
som = ['soma','Soma','SOMA'] # soma
subt = ['subtração','Subtração','SUBTRAÇÃO'] # subtração
mul = ['multiplicação','Multiplicação','MULTIPLICAÇÃO'] # multiplicação
div = ['divisão','Divisão','DIVISÃO'] # divisão

# calculos

def soma(): # SOMA
    somar = s1 + s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {somar:.2f}') # imprimi o resultado

def sub(): # SUBTRAÇÃO
    subtrair = s1 - s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {subtrair:.2f}') # imprimi o resultado

def multi(): # MULTIPLICAÇÃO
    multiplicar = s1 * s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {multiplicar:.2f}') # imprimi o resultado

def divi(): # DIVISÃO
    dividir = s1 // s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {dividir:.2f}') # imprimi o resultado

# calculos

s1 = float(input('Digite um numero: ')) # coleta o primeiro valor
s2 = float(input('Digite outro numero: ')) # coleta o segundo valor

esc = str(input('Qual tipo de calculo deseja executar? ')) # coleta o tipo de calculo

if esc in som: # se for soma
    soma()

if esc in subt: # se for subtração
    sub()

if esc in mul: # se for multiplicação
    multi()

if esc in div: # se for divisão
    divi()

else:# para valores inválidos
    print('Invalido')



