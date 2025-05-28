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
    print('COTAÇÂO DO DOLAR R$ 5,65 (data: 24/05/2025)\n')
    rsd = float(input('\nReal BR: R$ '))
    dl = rsd / 5.65
    print(f'Dolar USA: {dl:.2f} USD')
    print(f'R$ {rsd:.2f} ta valendo {dl:.2f} USD\n')

elif qm == 'iene':
    print('-' * 44)
    print('COTAÇÂO DO IENE R$ 0,040 (data: 24/05/2025)\n')
    rsi = float(input('\nReal BR: R$ '))
    ie = rsi / 0.040
    print(f'Iene JP: {ie:.2f} JPY')
    print(f'R$ {rsi:.2f} ta valendo {ie:.2f} JPY\n')

elif qm == 'euro':
    print('-' * 44)
    print('COTAÇÂO DO EURO R$ 6,42 (data: 24/05/25)')
    rse = float(input('\nReal BR: R$ '))
    eu = rse / 6.42
    print(f'Euro UE: {eu:.2f} EU')
    print(f'R$ {rse:.2f} ta valendo {eu:.2f} EU\n')
    print('-' * 44)

else:
    print('Moeda Invalida!')

print('\nReal ta valendo é nada...')
