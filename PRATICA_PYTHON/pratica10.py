#28.11.24
#COMANDO .FORMAT() - 02#

#O comando .format() tambem pode ser "diminuido" utilizando um f antes do 'texto' dentro do print como no exemplo abaixo


nome = str(input('Qual seu nome?'))

print(f'Olá {nome:-^20}')
print('Olá {:-^20}'.format(nome))