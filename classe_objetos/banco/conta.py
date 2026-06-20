class Conta:
    def __init__(self,clientes, numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = 0
        self.operacoes = []
        self.deposito(saldo)   
    
    def saque(self, valor):
        if  self.saldo >= valor:
               self.saldo -= valor
               self.operacoes.append(['SAQUE', valor])      
        else:
            print(f'SALDO INSUFICINTE, TENTATIVA DE SAQUE R$ {valor:.2f}') 
     
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPOSITO', valor])
    
    
    def extrato(self):
        print(f'EXTRATO CC N {self.numero}\n')
        for operacao in self.operacoes:
            print(f'{operacao[0]} {operacao[1]:10.2f}')
        print(f'\n saldo {self.saldo:10.2f}\n') 
          
    def resumo(self):
        print(f'CONTA N {self.numero}')
        for cliente in self.clientes:
            print(cliente.nome, cliente.telefone)
       
                
            
           
       

             
        
              
