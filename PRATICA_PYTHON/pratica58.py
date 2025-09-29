#08.08.25 - 27.09.25

from bancodenomes import sim_sim

#hora = float(input('Horas:'))
#anos = int(input('Anos:'))

eR = '🕐'
eC= '📅'

print(f'{eR} Conversor horas em anos e anos em horas {eC}\n')

print('O que você quer converter?')
qual = int(input('Para: \n(1) anos em horas  \n(2) horas em anos \n(3) horas em dias \n(4) dias em horas \nDigite aqui: '))
print(' ')

um_ano = 365
ano_hora = 8766
dia = 24
hora = 24

def convercao_ah(ano_p_hora): # converter anos para horas
    return anos * ano_hora

def convercao_ha(hora_p_ano): # converter horas para anos
    return horas / ano_hora

def convercao_hd(hora_p_dia):
    return horas / dia

def convercao_dh(dia_p_hora):
    return dias * hora

if qual == 1:

    anos = int(input('Digite quantos anos: '))

    convAH = convercao_ah(ano_hora)
    #convAH = anos * ano_hora

    print(' ')
    print(f'{anos} anos são {convAH} hora/as.')

elif qual == 2:

    horas = float(input('Digite quantos horas: '))

    convHA = convercao_ha(horas)
        #convHA = horas / ano_hora

    print(' ')
    print(f'{horas:.0f} horas são {convHA:.5f} anos.\n')
    print(' ')

    ex = input('Precisa do numero mais exato(s/n)? ')

    if ex in sim_sim:

        print(' ')
        print(f'{horas} horas são {convHA} ano/os.')

#___________________________________________________________________________________________________________________________

elif qual == 3:

    horas = float(input('Digite quantos horas: '))

    convHD = convercao_hd(horas)

    print(' ')
    print(f'{horas} horas são {convHD:.5f} dia/as.')
    print(' ')

    ex = input('Precisa do numero mais exato(s/n)? ')

    if ex in sim_sim:

        print(' ')
        print(f'{horas} horas são {convHD} dia/as.')

elif qual == 4:

    dias = int(input('Digite quantos dias: '))

    convDH = convercao_dh(dias)

    print(' ')
    print(f'{dias:.0f} dia/as são {convDH} hora/as.')

else:
    print(' ')
    print('Entrada Invalida!')

#hora_p_ano = hora / ano_hora
#ano_p_hora = anos * ano_hora
#print(hora_p_ano)
#print(ano_p_hora)