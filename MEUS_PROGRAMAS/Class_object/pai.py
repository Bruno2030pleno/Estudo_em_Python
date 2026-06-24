class Pai:
    def __init__(self, nome, idade, proposito):
        self.nome = nome
        self.idade = idade
        self.proposito = proposito
    
    def falar_meu_nome(self):
        if self.nome == 'Bruno':
           print(f"olã, me chamo {self.nome}")
    def falar_minha_idade(self):
        if self.idade == 35:
            print(f"eu tenho {self.idade} anos")
    def meu_proposito_de_vida(self):
        print(f"meu proposito de vida: {self.proposito}")      
                        
pasando_objeto = Pai("Bruno", 35, 'quero vencer na vida e proveitar minha familia\
e conseguir um emprego como desenvolvedor e criar minha empresa de tecnologia')

pasando_objeto.falar_meu_nome()
pasando_objeto.falar_minha_idade()
pasando_objeto.meu_proposito_de_vida()