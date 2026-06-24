class BancoException(Exception):
    pass

class SaldoInsuficiente(BancoException):
    pass


class ClienteNãoExiste(BancoException):
    pass

def saque(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficiente
    return saldo - valor
try:
    saldo = saque(100, 50)
except SaldoInsuficiente:
    print("Erro: Saldo insuficiente!!!")

# podemos tambem criar novas exceções que adicinem informaçoes ou atributos

class EstoqueException(Exception):
    def __init__(self, mensagem, codigo_de_erro):
        super().__init__(mensagem)
        self.codigo_de_erro = codigo_de_erro
def verifica_quantidade(quantidade):
        if quantidade <  0:
            raise EstoqueException("quantidade negativa", codigo_de_erro=1)
try:
    verifica_quantidade(-10)
except EstoqueException as ee:
        print(f"erro: {ee.codigo_de_erro} {ee}")            