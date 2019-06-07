import datetime

class Produto():
    '''Produto(nome,preco)'''
    def __init__(self, nome, preco):
        self.nome = CharField
        self.preco = preco

class Item():
    '''Item(produto,qtd)'''
    def __init__(self, produto, qtd):
        self.produto = produto
        self.qtd = qtd

    def get_preco(self):
        return self.produto.preco * self.qtd

class Carrinho():
    '''Carrinho(data,hora,itens)'''
    def __init__(self, itens):
        self.set_data()
        self.set_horario()
        self.itens = itens
        
    def get_preco(self):
        preco = 0
        for item in self.itens:
            preco += item.get_preco()
        return preco
    
    def set_data(self):
        ano = datetime.datetime.now().year
        mes = datetime.datetime.now().month
        dia = datetime.datetime.now().day
        self.data = "{}/{}/{}".format(dia,mes,ano)
    
    def set_horario(self):
        hora = datetime.datetime.now().hour
        minuto = datetime.datetime.now().minute
        self.horario = "{}:{}".format(hora,minuto)

if __name__=='__main__':
    shampoo = Produto('shampoo', 5)
    carne = Produto('carne', 10)
    item_shampoo= Item(shampoo, 1)
    item_carne = Item(carne, 2.5)
    carrinho = Carrinho([item_shampoo, item_carne])
    print('Preco correto shampoo: {}'.format(item_shampoo.get_preco()==5))
    print('Preco correto carne: {}'.format(item_carne.get_preco()==25))
    print('Preco correto carrinho: {}'.format(carrinho.get_preco()==30))
