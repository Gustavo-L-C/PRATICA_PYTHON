#04.12.24
#PRATICA - 05#

#Criar programa que LEIA a quantidade de dinheiro de uma pessoa e converta para dolar/iene/euro:

print(f'\n{" COTAÇÂO DO DOLAR / IENE / EURO ":*^40}\n')

qm = str(input('Qual a Moeda (dolar/iene/euro)? '))
#print('Digite abaixo sua quantidade de R$.')
#rs = float(input('\nReal BR: R$ '))
print(' ')

data = '28/05/205'
dl = 5.69
ie = 0.039
eu = 6.43



if qm == 'dolar':
    print('-' * 44)
    print(f'\033[34mCOTAÇÂO DO DOLAR R$ {dl} (data: {data})')
    rsd = float(input('Real BR: R$ '))
    cdl = rsd / dl
    print(f'Dolar USA: {cdl:.2f} USD')
    print(f'R$ \033[32m{rsd:.2f}\033[34m ta valendo \033[32m{cdl:.2f}\033[34m USD')
    print('\033[m-' * 44)
    print('\n\033[mReal ta valendo é nada...')

elif qm == 'iene':
    print('-' * 44)
    print(f'\033[31mCOTAÇÂO DO IENE R$ {ie} (data: {data})\n')
    rsi = float(input('Real BR: R$ '))
    cie = rsi / ie
    print(f'Iene JP: {cie:.2f} JPY')
    print(f'R$ \033[32m{rsi:.2f}\033[31m ta valendo \033[32m{cie:.2f}\033[31m JPY')
    print('\033[m-' * 44)
    print('\n\033[mReal ta valendo é nada...')

elif qm == 'euro':
    print('-' * 44)
    print(f'\033[33mCOTAÇÂO DO EURO R$ {eu} (data: {data})')
    rse = float(input('Real BR: R$ '))
    ceu = rse / eu
    print(f'Euro UE: {ceu:.2f} EU')
    print(f'R$ \033[32m{rse:.2f}\033[33m ta valendo \033[32m{ceu:.2f}\033[33m EU')
    print('\033[m-' * 44)
    print('\n\033[mReal ta valendo é nada...')

else:
    print('\033[31mMoeda Invalida!')


