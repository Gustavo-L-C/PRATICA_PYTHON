#17.06.25

#PRATICA

from bancodenomes import bancos_nomes

nome1 = str(input('\nQual seu nome? '))

class OLA:

    def ola(self, nome):
        self.nome = nome

    def imprimir(self):

        if nome1 in bancos_nomes:
            print('\033[33mOlá seja bem-vindo,', nome1, '\033[m')
        else:
            print('Seja bem-vindo,', nome1)

ola = OLA()
ola.imprimir()
