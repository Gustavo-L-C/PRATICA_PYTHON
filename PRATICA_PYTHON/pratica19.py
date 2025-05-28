#04.12.24
#PRATICA - 05#

#Criar programa que LEIA a quantidade de dinheiro de uma pessoa e converta para dolar/iene/euro:

print(f'\n{" COTAÇÂO DO DOLAR / IENE / EURO ":*^40}\n')

qm = str(input('Qual a Moeda (dolar/iene/euro)? '))
#print('Digite abaixo sua quantidade de R$.')
#rs = float(input('\nReal BR: R$ '))
print(' ')

#dl = rs / 5.65
#ie = rs / 0.040
#eu = rs / 6.42



if qm == 'dolar':
    print('-' * 44)
    print('\033[34mCOTAÇÂO DO DOLAR R$ 5,65 (data: 24/05/2025)')
    rsd = float(input('Real BR: R$ '))
    dl = rsd / 5.65
    print(f'Dolar USA: {dl:.2f} USD')
    print(f'R$ \033[32m{rsd:.2f}\033[34m ta valendo \033[32m{dl:.2f}\033[34m USD\n')
    print('\033[mReal ta valendo é nada...')
    print('-' * 44)

elif qm == 'iene':
    print('-' * 44)
    print('\033[31mCOTAÇÂO DO IENE R$ 0,040 (data: 24/05/2025)\n')
    rsi = float(input('Real BR: R$ '))
    ie = rsi / 0.040
    print(f'Iene JP: {ie:.2f} JPY')
    print(f'R$ \033[32m{rsi:.2f}\033[31m ta valendo \033[32m{ie:.2f}\033[31m JPY\n')
    print('\033[mReal ta valendo é nada...')
    print('-' * 44)

elif qm == 'euro':
    print('-' * 44)
    print('\033[33mCOTAÇÂO DO EURO R$ 6,42 (data: 24/05/25)')
    rse = float(input('Real BR: R$ '))
    eu = rse / 6.42
    print(f'Euro UE: {eu:.2f} EU')
    print(f'R$ \033[32m{rse:.2f}\033[33m ta valendo \033[32m{eu:.2f}\033[33m EU\n')
    print('\033[mReal ta valendo é nada...')
    print('-' * 44)

else:
    print('\033[31mMoeda Invalida!')


