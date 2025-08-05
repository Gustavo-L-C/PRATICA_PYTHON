#01.06.25
#ESTRUTURAS DE REPETIÇÂO - 03

from random import randint

#FOR - 02
#for i in range(x):
#para cada "i" dentro do "range(quantidade de repetições)":

#Exemplos:

ran = randint(1, 2)

for ran in range(5):
    if ran == 1:
        print('Toma')
    else:
        print('Meh')

print('\n.................................................................................................................\n')

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for numero in lst:
    if numero >= 50:
        cl = numero* 10
        print(cl)
    else:
        cl = numero / 10
        print(cl)

print('\n.................................................................................................................\n')

lst2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]

tttx = 0

for numero2 in lst2:
    if numero2 >= 870:
        tx = 0.2
    else:
        tx = 0.1

    txc = numero2 * tx
    tttx = tttx + txc # ou tttx += txc
    print(f'\nValor da taxa: {tx * 100}%\nValor: {numero2}\nTaxa: {txc}')

print(f'\nTaxa Total: {tttx}')
