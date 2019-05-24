class Item():
    '''Item(produto,qtd)'''
    def __init__(self, produto, qtd):
        self.produto = produto
        self.qtd = qtd

    def get_preco(self):
        return self.produto.preco * self.qtd