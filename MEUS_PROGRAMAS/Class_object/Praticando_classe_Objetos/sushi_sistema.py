
class Sushi:
    def __init__(self, nome, preco_base, quantidade):
        self.nome = nome
        self._preco_base = preco_base
        self.quantidade = quantidade

    @property
    def preco_final(self):
        total = self._preco_base * self.quantidade
        if self.quantidade > 10:
            return total * 0.95
        return total


class Pedido:
    def __init__(self, lista_de_sushis):
        self.lista = lista_de_sushis

    def exibir_comanda(self):
        for sushi in self.lista:
            print(f"{sushi.nome} - R$ {sushi.preco_final:.2f}")
    

class NovaException(Exception):
    pass

def lançador():
    raise NovaException("Exceção lançada!")  # aqui você lança
   

try:
    lançador()
except NovaException as e:
    print(e)       





temaki = Sushi("temaki", 8.80, 20)
uramaki = Sushi("uramaki", 5.00, 50)  # quantidade > 10, ganha desconto
maki = Sushi('maki salmão', 8, 100)


pedido = Pedido([temaki, uramaki, maki])
pedido.exibir_comanda()

