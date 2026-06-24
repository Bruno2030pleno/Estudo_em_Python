class Estoque:
    def __init__(self, produto, quantidade, validade):
        self.produto = produto
        self.quantidade = quantidade
        self.validade = validade
    
    def __str__(self):
            return f'produto {self.produto}' 
    
    def Nome_do_produto(self):
        print(f'Nome do produto {self.produto}')
    
    def quantidade_produto(self):
        print(f'quantidade de produtos no estoque {self.quantidade}')  
    
    def validade_dos_produtos(self):
        print(f'validade dos produtos {self.validade}')
            
nome = Estoque('arroz', 100, '10/08/2026')

nome.Nome_do_produto()
nome.quantidade_produto()
nome.validade_dos_produtos()
print(nome)
