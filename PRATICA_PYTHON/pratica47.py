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

def soma1(n1, n2):
    soma1 = n1 + n2
    print(soma1)
soma1(n1, n2)

#---------------------------------------------------------------------------

def soma2(n1, n2):
    soma2 = n1 + n2
    return soma2
resultado = soma2(n1, n2)
print(resultado)

#---------------------------------------------------------------------------

def par_impar(n1):
    if n1 % 2 == 0:
        return True
    else:
        return False

if par_impar(n1):
    print("Par")
else:
    print("Impar")