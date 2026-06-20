# from datetime import datetime as t

# class Pessoa:
#     def __init__(self, nome, idade, dt): # construtor
#         self.nome = nome
#         self.idade = idade
#         self.dt = t.strptime(dt, '%d/%m/%Y')
#     def exibir_dados(self): # metodos
#         print(f"meu nome {self.nome} minha idade {self.idade} minha data de nascimento {self.dt.strftime('%d/%m/%Y')}")    

# pessoa1 = Pessoa('jose', 35, '19/03/1991') # passando os ojbetos
# pessoa1.exibir_dados()
   
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Pessoa:
    nome: str
    idade: int
    dt: datetime

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Nasc: {self.dt.strftime('%d/%m/%Y')}")