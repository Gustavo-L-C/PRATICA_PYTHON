#04.12.24
#TRANSFORMAÇÂO DE STRIGNS#

f = '  HELLO WORLD!  '
f2 = 'hello world!'
f3 = 'HELLO WORLD!'

print('1-', f2.replace('hello', 'OLA')) #substitui palavras na string

print('2-', f2.upper()) #transforma todas as letras em letras maisculas

print('3-', f3.lower()) #tranforma todas as letras em letras minusculas

print('4-', f3.capitalize()) #formata a string deixando somente a primeira letra como maiscula

print('5-', f2.title()) #formata a string deixando a primeira palavra e cada outra palavra após um espaço com letras maisculas

print('6-', f.strip()) #remove espaços não necessarios tanto no inicio quanto no fim de um string

print('7-', f.rstrip()) #remove espaços finais não necessarios da string

print('8-', f.lstrip()) #remove espaços iniciais não necessarios da string