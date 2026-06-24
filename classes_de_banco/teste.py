from cliente import Cliente
from conta import Conta, ContaEspecial



bruno = Cliente('jose bruno', 'tel - 098765') # PASSANSO O METADO
maria = Cliente('maria lena', 'tel - 234455') # CLASSE CLIENTE


conta1 = Conta([bruno], numero=1, saldo=1000)
conta2 = ContaEspecial([maria], numero=2, saldo=500, limite=100)  


# conta1.saque(20)
# conta1.deposito(0)
# conta1.resumo()
# conta1.extrato()


resultado = conta2.saque(1000)
print(resultado)
conta2.extrato()







