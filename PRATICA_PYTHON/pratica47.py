#09.06.25
#FUNÇÕES - 01

# DEF - 01

def nome():
    no = str(input("Digite seu nome: "))
    def imprimir():
        print(no)
    imprimir()
nome()

#---------------------------------------------------------------------------

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

def soma(n1, n2):

    soma = n1 + n2
    print(soma)

soma(n1, n2)