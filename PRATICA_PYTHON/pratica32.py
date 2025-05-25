#25.05.2025
#MÃO LIVRE - 00

#leia dois valoras entre horas, minutos e segundos e transforme
# 1- horas em minutos
# 2- minutos em segundos
# 3- segundos em minutos
# 4- minutos em horas:
# depois imprima o resultado

# 01 horas = 60 minutos = 3600 segundos

t = 60
s = 3600

oqt1 = str(input('o que vamos transformar (horas, minutos, segundos)? '))
oqt2 = str(input('Em que iremos transformar (horas, minutos, segundos)? '))



if oqt1 == 'horas' and oqt2 == 'minutos': #1-horas em minutos
    qh1= int(input('Digite a quantidade de horas: '))

    hm = qh1 * t

    print(f'{qh1: .0f} horas são {hm: .0f} minutos')

elif oqt1 == 'minutos' and oqt2 == 'segundos': #2-minutos em segundos
    qh2= int(input('Digite a quantidade de minutos: '))

    hs = qh2 * s

    print(f'{qh2: .0f} minutos são {hs: .0f} segundos')

if oqt1 == 'segundos' and oqt2 == 'minutos': #3-segundos em minutos
    qh3= int(input('Digite a quantidade de segundos: '))

    sm= qh3 / t

    print(f'{qh3: .0f} segundos são {sm: .0f} minutos')

elif oqt1 == 'minutos' and oqt2 == 'horas': #4-minutos em horas
    qh4= int(input('Digite a quantidade de minutos: '))

    mh = qh4 / t

    print(f'{qh4: .0f} minutos são {mh: .0f} horas')




