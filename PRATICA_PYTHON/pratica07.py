#28.11.24
#OPERADPRES ARITMETICOS - 02#

# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // divisão de inteiros
# % resto da divisão


n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))

p = n1 ** n2
p1 = pow(n1, n2)
di = n1 // n2
r = n1 % n2

print('o resultado da potênicação de {0} elevado a {1} é {2}'.format(n1, n2, p))
print('o resultado da potênicação de {0} elevado a {1} é {2}'.format(n1, n2, p1))
print('a divisão de inteiros de {0} e {1} é igual a {2}'.format(n1, n2, di))
print('o resto da divisão entre {0} e {1} é igual a {2}'.format(n1, n2 ,r))