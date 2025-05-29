#23.05.25
#Formulário Simples


#Faça um formulário Simples que leia o nome, email, idade, ano de nascimento e cpf de uma pessoa e depois a imprima essas inforamções:

print('Bem-Vindo\n')

n = str(input('Digite seu nome completo: ')) #entrada de valor (nome)
e = str(input('Digite seu melhor email: ')) #entrada de valor (email)
i = int(input('Digite sua idade: ')) #entrada de valor (idade)
d = int(input('Digite o ano de nascimento: ')) #entrada de valor (data de nascimento)
c = int(input('Digite seu cpf: ')) #entrada de valor (cpf)


print(f'-----------------------------------\n') #só enfeite

print(f'Seu cadastro\n nome: {n}\n email: {e}\n idade: {i}\n ano: {d}\n cpf: {c}')# imprimir todas as informações coletadas

print(f'\n-----------------------------------') #só enfeite

print('Cadastro finalizado com sucesso!')
print(f'\nSeja Bem-Vindo {n}')