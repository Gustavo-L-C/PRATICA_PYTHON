#10.01.25
#PRATICA - 09#
n = str(input('Digite seu nome: '))
s = str(input('Digite a senha: '))

if s == '1234570':
    print(f'Acesso permitido, seja bem-vindo de volta {n}.')

else:
    print('Acesso negado, já possui cadastro?')
    print('.......')
    print('.......')
    print('.......')

    n2 = str(input('Digite seu nome: '))
    s2 = str(input('Digite sua senha: '))

    print('.......')
    print('.......')
    print('.......')

    print(f' Olá {n2}, seja bem-vindo')
    s3 = input('Digite sua senha: ')
    print('.......')

    if s3 == s2:
       print('...')
       print('..')
       print('...')
       print(f'Acesso permitido, seja bem-vindo {n2}!')
    else:
        print('Acesso negado!')
        print('.......')
        print('.......')
        print('.......')


print('Seu acesso foi negado, tente novamente mais tarde....')