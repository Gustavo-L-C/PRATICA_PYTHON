#17.06.25

#PRATICA

from bancodenomes import bancos_nomes # banco de nomes

# _________________________________________________________________________________________________________________

nome1 = str(input('Digite seu nome: ')) # coletar o nome

# _________________________________________________________________________________________________________________

if nome1 in bancos_nomes: # se o nome coletado estiver dentro do banco de nomes
    salario1 = 2000 # salario igual a 2000

else: # se não
    salario1 = 1500 # salario igual a 1500

# _________________________________________________________________________________________________________________

class Emp: # classe Emp (empregado)

    def __init__(self, nome, salario): # função inicial nome e salario
        self.nome = nome
        self.salario = salario

    def imprime(self): # função para imprimir na tela
        print(f'{self.nome} tem um salário de R$ {self.salario:.2f}')

emp = Emp(nome1, salario1)
emp.imprime()

# _________________________________________________________________________________________________________________
