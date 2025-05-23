#10.01.25
#PRATICA - 08#

n = str(input('Qual seu nome? '))
s = input('Digite a senha: ')


if n == 'Gustavo' and s == 'glc1234570':
    print(f'\nSeja Bem-Vindo de volta {n} :)')
    print('ACESSO PERMITIDO')

elif n == 'Gustavo':
    s1 = input(f'Senha Incorreta tente novamente {n}: ')
    if s1 == '1234567':
        print(f'\nSeja Bem-Vindo de volta {n} :)')
        print('ACESSO PERMITIDO')

else:
    print(f'XXXXXXXXXXXXXXXXXXX\nOlá...')
    n1 = input(f'Quem está ai? ')
    if n1 == 'Gustavo':
        s2 = input(f'Algo errado tente novamente {n}: ')
        if s2 == '1234567':
            print(f'\nSeja Bem-Vindo de volta {n} :)')
            print('ACESSO PERMITIDO')
        else:
            print(f'Oque o traz aqui {n1}?....')
            print('É melhor ir embora ^_^')
            print('ACESSO NEGADO')

