class Produto:
    def __init__(self, cod, descricao, fabricante, quantidade=0):
        self.cod = cod
        self.descricao = descricao
        self.fabricante = fabricante
        self.quantidade = quantidade