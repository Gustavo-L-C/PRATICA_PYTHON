#17.06.25

#PRATICA

from bancodenomes import bancos_nomes # banco de nomes

nome1 = str(input('Digite seu nome: ')) # coletar o nome

if nome1 in bancos_nomes:

    salario1 = 2000

else:

    salario1 = 1500

class Emp:
    def __init__(self, nome, salario):

        self.nome = nome

        self.salario = salario

    def imprime(self):

        print(f'{self.nome} tem um salário de R$ {self.salario:.2f}')

emp = Emp(nome1, salario1)

emp.imprime()