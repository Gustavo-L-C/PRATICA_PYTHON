#10.01.24
#PRATICA - 10#

#TAXA OU NÂO TAXA
#PS. SEMPRE VAI TAXAR

# produto x + frete > 50 USD = taxa de 20% dos 50 mais taxa de 60% do valor excedente
# produto x + frete <= 50 USD = taxa 20%

print('TAXA SOBRE IMPORTAÇÃO\n')

ql = str(input('Em qual Loja você irá importar seu produto? '))
vp = float(input('Qual Valor do produto(R$)? '))
ft = float(input('E qual o valor do frete(R$)? '))
print('')

vdl = 5.67 #valor do dólar da data: 20/05/2025, horário: 14:59#
txm = 50 #valor atual da taxa (11/01/2025) em dólares
txm50 = 60 #valor da % de produtos excedentes a 50 dólares
txb50 = 20 #%valor da % de produtos de até 50 dólares
rsdl = txm * vdl #taxa 50 dólares x valor do dólar
dl50 = rsdl / vdl #valor convertido / valor do dólar
cvp = vp / vdl #valor do produto / valor do dólar
cft = ft / vdl #valor do frete / valor do dólar

tt = cvp + cft#total = valor do produto convertido + valor do frete convertido

if tt >= 50:
    print(f'Sua compra na {ql} deu um total de {tt:.2f} dólares e você foi taxado...')
    tx2050 = (txb50 / 100) * dl50 #taxa de 50 dólares 20% de 50 dólares
    tx60 = (txm50 / 100) * (tt - txm) #taxa do valor excedente 60% do valor excedente a 50 dólares
    ctx60 = (tx60 + tx2050) * vdl #valor da taxa total convertida
    vtdctx60 = vp + ft + ctx60
    print(f'O valor da sua taxa será de aproximadamente {tx60 + tx2050:.2f} dólares, que é dividido em 20% do valor de 50 dólares mais 60% do valor excedente aos 50 dólares, ou seja, R$ {ctx60:.2f}, dando um total de R$ {vtdctx60:.2f}...')
    print('\nPS. Não tem como fujir da taxação...\nE essa é só a taxa de importação....')

else:
    print(f'Sua compra na {ql} deu um total de {tt:.2f} dólares e você foi taxado em 20%...')
    tx20 = (txb50 / 100) * tt #valor da taxa de 20% de produtos até 50 dólares
    ctx20 = tx20 * vdl #valor da taxa total convertida
    vtdctx20 = vp + ft + ctx20
    print(f'O valor da sua taxa será de aproximadamente {tx20:.2f} dólares, ou seja, R$ {ctx20:.2f}, dando um total de R$ {vtdctx20:.2f}...')
    print(
        '\nPS. Não tem como fujir da taxação...\nE essa é só a taxa de importação....')