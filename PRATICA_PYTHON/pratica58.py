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

if qual == 1:
    anos = int(input('Digite quantos anos: '))

    ano_p_hora = anos * ano_hora

    print(' ')
    print(f'{anos} anos são {ano_p_hora} horas.')

else:
    if qual == 2:
        horas = float(input('Digite quantos horas: '))

        hora_p_ano = horas / ano_hora

        print(' ')
        print(f'{horas:.0f} horas são {hora_p_ano:.5f} anos.\n')

        ex = input('Precisa do numero mais exato(s/n)?')

        if ex in sim_sim:

            print(' ')
            print(f'{horas} horas são {hora_p_ano} anos.')
            
#hora_p_ano = hora / ano_hora
#ano_p_hora = anos * ano_hora
#print(hora_p_ano)
#print(ano_p_hora)


