from passagem_de_parametros import Televisao  # Importa a classe do outro arquivo
class ControleRemoto:
    def __init__(self, televisão, pilha):
        self.televisão = televisão
        self.pilha = pilha  
    def liga(self):
        if self.pilha.consuma(1):
            self.televisão.ligada = True
    def desliga(self):
        if self.pilha.consuma(1):
            self.televisão.ligada = False
    def canal_mais(self):
        if self.pilha.consuma(1):
           self.televisão.c_cima()
    def canal_menos(self):
        if self.pilha.consuma(1):
            self.pilha.c_cima()

class Bateria:
    def __init__(self, energia=100):
        self.energia = energia
    def consuma(self, consumo):
        if consumo > self.energia:
            consumo = self.energia
        self.energia -= self.consumo
        return consumo
    
tv = Televisao(0, 20)
controle = ControleRemoto(tv)
print(tv.canal)
print(tv.ligada)
controle.liga()
print(tv.ligada)


