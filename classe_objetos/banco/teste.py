from cliente import Cliente
from conta import Conta

bruno = Cliente('jose bruno', 'tel - 098765') # PASSANSO O METADO
maria = Cliente('maria lena', 'tel - 234455') # CLASSE CLIENTE
joao = Cliente('joao mario', 'tel - 1234-456')
jose = Cliente('jose maria', 'tel - 23456-65')

conta1 = Conta([bruno], 1, 1000)
conta2 = Conta([maria,bruno], 2, 800)  # CLASSE CONTA
conta3 = Conta([joao, jose], 3, 500)
# CHAMANDO O METADO QUE SAO AS FUNCIONALIDADE DAS CLASSSES

conta1.saque(20)
conta1.deposito(0)
conta1.extrato()

conta2.saque(3000)
conta2.deposito(100)
conta2.extrato()
conta2.resumo()
conta3.saque(200)
conta3.deposito(150)
conta3.resumo()
conta3.extrato()





