#08.08.25

#hora = float(input('Horas:'))
#anos = int(input('Anos:'))

eR = '🕐'
eC= '📅'

print(f'{eR} Conversor horas em anos e anos em horas {eC}\n')

print('O que você quer converter? ')
qual = int(input('Digite (1) para anos em horas e (2) para horas em anos: '))

um_ano = 365
ano_hora = 8766

if qual == 1:
    anos = int(input('Digite quantos anos: '))

    ano_p_hora = anos * ano_hora

    print(f'{anos} anos são {ano_p_hora} horas.')

else:
    if qual == 2:
        horas = float(input('Digite quantos horas: '))

        hora_p_ano = horas * ano_hora

        

#hora_p_ano = hora / ano_hora
#ano_p_hora = anos * ano_hora

#print(hora_p_ano)

#print(ano_p_hora)


