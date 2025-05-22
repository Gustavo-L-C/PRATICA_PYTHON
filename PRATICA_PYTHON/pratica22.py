#04.12.24
#ANALISE DE STRIGNS#

f = 'HELLO WORLD!'

print('1-', len(f)) #diz o tamanho da string

print('2-', f.count('HELLO')) #conta letras ou palavras na string

print('3-', f.find('LL')) #procura dentro da string

print('4-', f.find('GG')) #observação quando não é encontrado o que buscado dentro da string o resultado é sempre -1,
                          #visto que, sempre se conta de 0 a avante dentro do Python.

print('5-', 'HELLO' in f) #procura dentro da string e diz se é True ou False