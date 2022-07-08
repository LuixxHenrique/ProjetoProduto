from Venda import *

class Salvar_Fabricante():
   def __init__(self, cod, nome):
        self.cod = cod
        self.nome = nome

class Fabricante():
    def __init__(self):
        self.fabr = []

    def cadastrar(self):
        ganha = int(input('código:\n'))
        ganhaNome = str(input('nome:\n'))
        self.fabr.append(Salvar_Fabricante(cod=ganha,
                                          nome=ganhaNome))
