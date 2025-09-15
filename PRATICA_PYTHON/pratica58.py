#08.08.25

from bancodenomes import sim_sim

#hora = float(input('Horas:'))
#anos = int(input('Anos:'))

eR = '🕐'
eC= '📅'

print(f'{eR} Conversor horas em anos e anos em horas {eC}\n')

print('O que você quer converter? ')
qual = int(input('Digite (1) para anos em horas e (2) para horas em anos: '))
print(' ')

um_ano = 365
ano_hora = 8766

def convercao_ah(ano_p_hora): # converter anos para horas
    return anos * ano_hora

def convercao_ha(hora_p_ano): # converter horas para anos
    return horas / ano_hora

if qual == 1:
    anos = int(input('Digite quantos anos: '))

    convAH = convercao_ah(ano_hora)
    #convAH = anos * ano_hora

    print(' ')
    print(f'{anos} anos são {convAH} horas.')

else:
    if qual == 2:
        horas = float(input('Digite quantos horas: '))

        convHA = convercao_ha(horas)
        #convHA = horas / ano_hora

        print(' ')
        print(f'{horas:.0f} horas são {convHA:.5f} anos.\n')

        ex = input('Precisa do numero mais exato(s/n)?')

        if ex in sim_sim:

            print(' ')
            print(f'{horas} horas são {convHA} anos.')

#hora_p_ano = hora / ano_hora
#ano_p_hora = anos * ano_hora
#print(hora_p_ano)
#print(ano_p_hora)