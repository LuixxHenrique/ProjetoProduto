from Compra import Compra
from classe_Fabricante import *
from Venda import *
from classe_Estoque import Estoque

class Menu:
    def __init__(self):
        self.i = Estoque()

        compra = Compra()
        compra.i_3 = self.i

        venda = Venda()
        venda.i_2 = self.i

        self.fabrica = Fabricante()
        self.i.entrada = self.fabrica

        while True:
            entrada = input('1- Cadastrar\n2'
                            '- Listar Produtos\n3'
                            '- Alterar Produto\n4'
                            '- Comprar\n5'
                            '- Vender\n6'
                            '- Cadastrar Fabricante\n7'
                            '- Sair\n')

            if entrada == '1':
                self.i.salvar_produtos()
            elif entrada == '2':
                self.i.listar_produtos()
            elif entrada == '3':
                self.i.alterar_produto()
            elif entrada == '4':
                compra.comprar()
            elif entrada == '5':
                venda.vender()
            elif entrada == '6':
                self.fabrica.cadastrar()
            elif entrada == '7':
                break