from classe_Estoque import Estoque

class Venda:
    def __init__(self):
        self.i_2 = Estoque()

    def vender(self):
        controle_venda = int(input('Informe o Código do Produto:\n'))
        for i in range(len(self.i_2.get)):
            if controle_venda == self.i_2.get[i].cod:
                self.i_2.get[i].quant -= \
                    int(input('Informe a Quantia para Venda:\n'))
            else:
                pass