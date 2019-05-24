from produto import Produto
from item import Item
from carrinho import Carrinho

if __name__=='__main__':
    shampoo = Produto('shampoo', 5)
    carne = Produto('carne', 10)
    item_shampoo= Item(shampoo, 1)
    item_carne = Item(carne, 2.5)
    carrinho = Carrinho([item_shampoo, item_carne])
    print('Preco correto shampoo: {}'.format(item_shampoo.get_preco()==5))
    print('Preco correto carne: {}'.format(item_carne.get_preco()==25))
    print('Preco correto carrinho: {}'.format(carrinho.get_preco()==30))
