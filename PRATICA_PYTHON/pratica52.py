#17.06.25

#PRATICA

from random import randint

def uma_senha(senha):
    us1 = randint(0,20)
    us2 = randint(0, 20)
    us3 = randint(0, 20)
    senha = [us1,us2,us3]
    print('Sua senha:', senha)

q = input('ola:')

if q in ['sim','ss','s']:
   uma_senha(q)

else:
    print('n')