#04.12.24
#PRATICA - 06#

#Criar um programa que LEIA a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
#tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2 m².

l = float(input('Qual a largura da sua parede: '))
a = float(input('Qual a altura da sua parede: '))

ar = l * a
t = ar / 2

print(f'Sua parede tem as dimensões de {l:.2f}x{a:.2f} e área de {ar}m².', end=' ')
print(f'e será necessário {t:.1f}L de tinta.')

