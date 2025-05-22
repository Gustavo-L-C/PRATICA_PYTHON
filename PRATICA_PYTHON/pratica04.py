#14.11.24
#COMANDO .FORMAT() - 01#

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

m = n1 * n2
s = n1 + n2
d = n1 / n2
su = n1 - n2

print('A multiplicação de {0} e {1} é igual a {2} '.format(n1, n2, m))
print('A soma de {0} e {1} é igual a {2} '.format(n1, n2, s))
print('A divisão de {0} e {1} é igual a {2} '.format(n1, n2, d))
print('A subtração de {0} e {1} é igual a {2} '.format(n1, n2, su))

#.format() basicamente substitui os valores entre {}, como nos exemplos acima
