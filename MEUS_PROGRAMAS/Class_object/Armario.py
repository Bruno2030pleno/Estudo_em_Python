class Armario:
    def __init__(self, gaveta):
        self.gaveta = gaveta
        self.lista = []
    # vamos desenvolver os metados do Armario
    
    def ação(self):
        self.escolhendo = input('qual ferramenta voce deseja adicionar na gaveta ?: ')
        self.lista.append(self.escolhendo)
        return 'metado realizado com sucesso'
    
    def conteudo(self):
        print(f'dono da gaveta {self.gaveta}')
        for dados, item in enumerate(self.lista):
            print(dados, item)
e = Armario('lena')
e.ação()
e.ação()
e.conteudo()