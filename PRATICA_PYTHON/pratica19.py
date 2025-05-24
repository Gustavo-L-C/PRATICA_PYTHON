#04.12.24
#PRATICA - 05#

#Criar programa que LEIA a quantidade de dinheiro de uma pessoa e converta para dolar/iene/euro:

print(f'\n{" COTAÇÂO DO DOLAR / IENE / EURO ":*^40}\n')


print('Digite abaixo sua quantidade de R$.')
rs = float(input('\nReal BR: R$ '))
print(' ')

dl = rs / 5.65
ie = rs / 0.040
eu = rs / 6.42

print('-'*44)
print('COTAÇÂO DO DOLAR R$ 5,65 (data: 24/05/2025)\n')


print(f'Dolar USA: {dl:.2f} USD')
print(f'R$ {rs:.2f} ta valendo {dl:.2f} USD\n')


print('-'*44)
print('COTAÇÂO DO IENE R$ 0,040 (data: 24/05/2025)\n')


print(f'Iene JP: {ie:.2f} JPY')
print(f'R$ {rs:.2f} ta valendo {ie:.2f} JPY\n')


print('-'*44)
print('COTAÇÂO DO EURO R$ 6,42 (data: 24/05/25)')

print(f'Euro UE: {eu:.2f} EU')
print(f'R$ {rs:.2f} ta valendo {eu:.2f} EU\n')
print('-'*44)

print('\nReal ta valendo é nada...')
