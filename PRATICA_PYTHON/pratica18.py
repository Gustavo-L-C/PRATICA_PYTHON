#04.12.24
#PRATICA - 04#

#Criar um programa que LEIA um valor em metros e exiba convertido em centimetros e milimetros

print('-' * 20)
m = float(input('Digite uma medida em metros(m): '))


cm = m * 100
mm = m * 1000
km = m / 1000

print(f'\n{m}m corresponde a {cm:.2f}cm, {mm:.2f}mm', end=' ')
print(f'e {km:.3f}km')
print('-' * 20)