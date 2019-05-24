import datetime

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