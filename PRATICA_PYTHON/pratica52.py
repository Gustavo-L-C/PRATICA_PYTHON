#17.06.25

#PRATICA

from random import randint
import secrets

def uma_senha(senha):

    us1 = randint(0,20)
    us2 = randint(0, 20)
    us3 = randint(0, 20)
    us4 = randint(0, 20)
    us5 = randint(0, 20)
    us6 = randint(0, 20)
    us7 = randint(0, 20)
    us8 = randint(0, 20)

    senha = [us1,us2,us3,us4,us5,us6,us7,us8]

    print('\n\033[35mSua senha:','\033[35m', senha)

def uma_senha_segura(senha_segura):

    print('\nSua senha:','\033[36m', secrets.token_bytes(10))

q = input('Olá que tipo de senha você precisa (\033[36msegura\033[m ou \033[35msimples\033[m)? ')

if q in ['simples', 'Simples', 'SIMPLES']:
   uma_senha(q)

if q in ['segura', 'Segura', 'SEGURA']:
    uma_senha_segura(q)

else:
    print('erro!!!')