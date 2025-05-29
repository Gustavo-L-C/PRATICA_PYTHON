#08.01.25
#PRATICA - 07#

#gerador de senhas

from random import randint

n = str(input('Qual seu nome? '))
s1 = 1
s2 = 60

se1 = randint(s1, s2)
se2 = randint(s1, s2)
se3 = randint(s1, s2)
se4 = randint(s1, s2)
se5 = randint(s1, s2)
se6 = randint(s1, s2)



if n == 'Gustavo' or 'gustavo' or 'GUSTAVO':
    print(f'\nBem-vindo de volta {n} :)')
    print('A senha do dia é ...', se1,se2,se3,se4,se5,se6)

else:
    print(f'\nOlá, {n}')
