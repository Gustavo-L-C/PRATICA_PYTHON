#28.05.25

print(f'\n{" 💱 CONVERSÂO DO DOLAR / IENE / EURO 💱 ":*^40}\n')

qm = str(input('Qual a Moeda (dolar/iene/euro)? '))

print(' ')

data = '28/05/205'
dl = 5.69
ie = 0.039
eu = 6.43



if qm in ['dolar', 'Dolar', 'DOLAR']:
    print('-' * 44)
    print(f'\033[34mCONVERSÂO DO DOLAR (data: {data})')
    rsd = float(input('Dólar: \033[32mUSD '))
    cdl = rsd * dl
    print(f'\033[34mCotação do Dolar USA: \033[32m{dl} USD\033[33m')
    print(f'\033[32m{rsd:.2f} USD\033[34m são \033[32mR$ {cdl:.2f}\033[34m')
    print('\033[m-' * 44)
    print('\n\033[mReal ta valendo é nada...')

elif qm in ['iene', 'Iene', 'IENE']:
    print('-' * 44)
    print(f'\033[31mCONVERSÂO DO IENE (data: {data})\n')
    rsi = float(input('Iene: \033[32mR$JPY '))
    cie = rsi * ie
    print(f'\033[31mCotação do Iene JP: \033[32m{ie} JPY\033[33m')
    print(f'\033[32m{rsi:.2f} JPY\033[31m são \033[32mR$ {cie:.2f}\033[31m')
    print('\033[m-' * 44)
    print('\n\033[mReal ta valendo é nada...')

elif qm in ['euro', 'Euro', 'EURO']:
    print('-' * 44)
    print(f'\033[33mCONVERSÂO DO EURO (data: {data})')
    rse = float(input('Euro: \033[32m€ '))
    ceu = rse * eu
    print(f'\033[33mCotação do Euro UE: \033[32m{eu} €\033[33m')
    print(f'\033[32m{rse:.2f} €\033[33m são \033[32mR$ {ceu:.2f}\033[33m')
    print('\033[m-' * 44)
    print('\n\033[mReal ta valendo é nada...')

else:
    print('\033[31mMoeda Invalida!')
