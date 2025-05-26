#25.05.2025
#MÃO LIVRE - 00

# leia duas medidas de tempo entre horas, minutos e segundos e transforme
# 1- horas em minutos
# 2- minutos em segundos
# 3- segundos em minutos
# 4- minutos em horas
# depois imprima o resultado


#valores
# 01 horas = 60 minutos = 3600 segundos

t = 60 #tempo
s = 3600 #60 minutos em segundos

#ler as duas medidas de tempo entre horas, minutos e segundos

#lendo..................................................................................................................
oqt1 = str(input('o que vamos transformar (horas, minutos, segundos)? '))
oqt2 = str(input('Em que iremos transformar (horas, minutos, segundos)? '))


#1......................................................................................................................
if oqt1 == 'horas' and oqt2 == 'minutos': #1-horas para minutos
    qh1= float(input('Digite a quantidade de horas: '))

    hm = qh1 * t # horas para minutos = horas * 60

    print(f'\nR: {qh1: .2f} horas são {hm: .2f} minutos') #imprimindo o resultado

#2......................................................................................................................
elif oqt1 == 'minutos' and oqt2 == 'segundos': #2-minutos para segundos
    qh2= float(input('Digite a quantidade de minutos: '))

    ms = qh2 * s # minutos para segundos = minutos * 3600

    print(f'\nR: {qh2: .2f} minutos são {ms: .2f} segundos') #imprimindo o resultado

#3......................................................................................................................
if oqt1 == 'segundos' and oqt2 == 'minutos': #3-segundos para minutos
    qh3= float(input('Digite a quantidade de segundos: '))

    sm= qh3 / t # segundos para minutos = segundos / 60

    print(f'\nR: {qh3: .2f} segundos são {sm: .2f} minutos') #imprimindo o resultado

#4......................................................................................................................
elif oqt1 == 'minutos' and oqt2 == 'horas': #4-minutos para horas
    qh4= float(input('Digite a quantidade de minutos: '))

    mh = qh4 / t # minutos para horas = minutos / 60

    print(f'\nR: {qh4: .2f} minutos são {mh: .2f} horas') #imprimindo o resultado

#extra1.................................................................................................................

if oqt1 == 'horas' and oqt2 == 'segundos': #extra-horas para segundos
    qh5= float(input('Digite a quantidade de horas: '))

    hs = qh5 * s # horas para segundos = horas * 3600

    print(f'\nR: {qh5: .2f} horas são {hs: .2f} segundos') #imprimindo o resultado

#extra2.................................................................................................................
elif oqt1 == 'segundos' and oqt2 == 'horas': #extra-segundos para horas
    qh6= float(input('Digite a quantidade de segundos: '))

    sh = qh6 / s # segundos para horas = segundos / 3600

    print(f'R: {qh6: .2f} segundos são {sh: .4f} horas') #imprimindo o resultado
