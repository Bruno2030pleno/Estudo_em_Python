class Conta:
    def __init__(self,clientes, numero, saldo=0):
        self.confirmacao = False
        self.clientes = clientes
        self.numero = numero
        self.saldo = 0
        self.operacoes = []
        self.deposito(saldo)   
    
    def posso_sacar(self, valor):
        return self.saldo >= valor   
    
    def saque(self, valor):
        if  self.saldo >= valor:
               self.saldo -= valor
               self.operacoes.append(['SAQUE', valor]) 
               return True
        else:
           print(f'SALDO INSUFICINTE, TENTATIVA DE SAQUE R$ {valor:.2f}')
          
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPOSITO', valor])
    
    def extrato(self):
        print('Banco Nubank')
        print(f'EXTRATO CC N {self.numero}\n')
        for operacao in self.operacoes:
            print(f'{operacao[0]} {operacao[1]:10.2f}') 
        print(f'\n SALDO {self.saldo:10.2f}\n') 
         
    def resumo(self):
        print(f'CONTA N {self.numero}')
        for cliente in self.clientes:
            print(cliente.nome, cliente.telefone)
       
class ContaEspecial(Conta):
    def __init__(self, clientes, numero,saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)  
        self.limite = limite 
    
    def posso_sacar(self, valor):  # ContaEspecial
        return (self.saldo + self.limite) >= valor

    def saque(self, valor):
        if self.posso_sacar(valor):
            return super().saque(valor)
        else:
            print(f'SALDO INSUFICIENTE, TENTATIVA DE SAQUE R$ {valor:.2f}')
            return False
                
    def extrato(self):
        super().extrato()
        print(f'limite da conta especial R$ {self.limite}') 
        print(f'Total em sua conta R$ {self.saldo + self.limite}')    
            
            
           
       

             
        
              
