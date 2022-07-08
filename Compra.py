from classe_Estoque import *

class Compra:
    def __init__(self):
        self.i_3 = Estoque()

    def comprar(self):
        controle = int(input('Informe o código do Produto:\n'))
        for i in range(len(self.i_3.get)):
            if controle == self.i_3.get[i].cod:
                self.i_3.get[i].quant += \
                    int(input('Informe a Quantia Comprada:\n'))
            else:
                pass