#02.06.25
#MÂO LIVRE - 01

# ICMS - Imposto sobre Circulação de Mercadorias e Prestação de Serviços
# cada estado brasileiro cobra um valor diferente no ICMS

print('_________________________________________________________________________________________________________________')
print('Índice de Estados')
print('_________________________________________________________________________________________________________________')
print('0- Acre\n1- Alagoas\n2- Piauí\n3- Rio Grande do Norte\n4- Amapá\n5- Amazonas\n6- Maranhão\n7- Bahia\n8- Ceará\n9- Distrito Federal\n10- Espírito Santo\n11- Goiás\n'
      '12- Mato Grosso\n13- Mato Grosso do Sul\n14- Minas Gerais\n15- Pará\n16- Paraíba\n17- Paraná\n18- Pernambuco\n19- Rio de Janeiro\n20- Rio Grande do Sul\n'
      '21- Rondônia\n22- Roraima\n23- Santa Catarina\n24- São Paulo\n25- Sergipe\n26- Tocantins')
print('_________________________________________________________________________________________________________________\n')

#0- Acre: 19,00%
AC = 0.19
#1- Alagoas: 20,00% (19% + 1% FECOEP)
AL = 0.2
#2- Piauí: 21,00% -
PI = 0.21
#3- Rio Grande do Norte: 18,00% -
RN = 0.18
#4- Amapá: 18,00% -
AP = 0.18
#5- Amazonas: 20,00% -
AM = 0.2
#6- Maranhão: 22,00% -
MR = 0.22
#7- Bahia: 20,50% -
BH = 0.205
#8- Ceará: 20,00% -
CE = 0.2
#9- Distrito Federal: 20,00% -
DF = 0.2
#10- Espírito Santo: 17,00% -
ES = 0.17
#11- Goiás: 19,00% -
GO = 0.19
#12- Mato Grosso: 17,00% -
MT = 0.17
#13- Mato Grosso do Sul: 17,00% -
MS = 0.17
#14- Minas Gerais: 18,00% -
MG = 0.18
#15- Pará: 19,00% -
PR = 0.19
#16- Paraíba: 20,00% -
PB = 0.2
#17- Paraná: 19,50% -
PN = 0.195
#18- Pernambuco: 20,50% -
PE = 0.205
##19- Rio de Janeiro: 22,00% (20,00% + 2,00% FECP) -
RJ = 0.22
#20- Rio Grande do Sul: 17,00% -
RS = 0.17
#21- Rondônia: 19,50% -
RN = 0.195
#22- Roraima: 20,00% -
RM = 0.2
#23- Santa Catarina: 17,00% -
SC = 0.17
#24- São Paulo: 18,00% -
SP = 0.18
#25- Sergipe: 20,00% (19% + 1% FECOEP) -
SE = 0.2
#26- Tocantins: 20,00% -
TO = 0.2

lista_de_E = [AC, AL, PI, RN, AP, AM, MR, BH, CE, DF, ES, GO, MT, MS, MG, PR, PB, PN, PE, RJ, RS, RN, RM, SC, SP, SE, TO]
Estados = ['Acre', 'Alagoas', 'Piauí', 'Rio Grande do Norte', 'Amapá', 'Amazonas', 'Maranhão', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco',' Rio de Janeiro', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']

ICMS_E = int(input(f'Qual seu Estado (de acordo com a numeração no índice de estados)? '))

if 0 <= ICMS_E < len(lista_de_E):
    valor_ICMS = float(lista_de_E[ICMS_E])

    estado = str(Estados[ICMS_E])

    print(f'O valor do ICMS do estado {estado} é de{valor_ICMS * 100: .0f}%')

else:
    print('ERRO')

print('\n_________________________________________________________________________________________________________________')

