#12.06.25
#FUNÇÕES - 04

# DEF - 04

# calculos

def soma(): # SOMA
    somar = s1 + s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {somar:.2f}')

def subtracao():
    subtrair = s1 - s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {subtrair:.2f}')

def multiplicacao():
    multiplicar = s1 * s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {multiplicar:.2f}')

def divisao():
    dividir = s1 / s2
    print(f'A {esc} entre {s1:.2f} e {s2:.2f} é igual a {dividir:.2f}')

# calculos

s1 = float(input('Digite um numero: ')) # recebendo o primeiro valor
s2 = float(input('Digite outro numero: ')) # recebendo o segundo valor

esc = str(input('Qual tipo de calculo deseja executar? ')) # recebendo o tipo de calculo

# listas facilitadoras
som = ['soma','Soma','SOMA']
sub = ['subtração','Subtração','SUBTRAÇÃO']
mul = ['multiplicação','Multiplicação','MULTIPLICAÇÃO']
div = ['divisão','Divisão','DIVISÃO']


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



