from Produto import *
from classe_Fabricante import *


class Estoque:
    def __init__(self):
        self.get = []
        self.get.append(Produto(5, 'Notebook', 'Teste', 0))
        self.entrada = Fabricante()

    def salvar_produtos(self):
        entrada_cod = int(input('Informe o Codigo: \n'))
        entrada_descricao = input('Informe a Descricao: \n')
        entrada_quantidade = int(input('Informe a Quantidade: \n'))
        fra = int(input('informe o Codigo do Fabricante: \n'))
        for fabri in range(len(self.entrada.fabr)):
            if fra == int(self.entrada.fabr[fabri].cod):
                self.get.append(Produto(cod=entrada_cod,
                                          descricao=entrada_descricao,
                                          fabricante=self.entrada.fabr[fabri].nome,
                                          quantidade=entrada_quantidade))
                print('Produto salvo!')
            else:
                print('Fabricante Nao Encontrado!')

    def listar_produtos(self):
        for i in range(len(self.get)):
            print('Cod:\n', self.get[i].cod,
                  '\nDescricao:\n', self.get[i].descricao,
                  '\nFabricante:\n', self.get[i].fabricante,
                  '\nQuantidade\n',
                  self.get[i].quantidade)

    def alterar_produto(self):
        colocar = input('Informe o codigo do produto: \n')
        for i in range(len(self.get)):
            if colocar == self.get[i].cod:
                self.get[i].descricao = input('Digite a Nova Descricao: \n')
