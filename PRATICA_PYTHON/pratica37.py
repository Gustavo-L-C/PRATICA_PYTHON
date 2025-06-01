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
