# minha tv
class Televisao:
    def __init__(self, canal_min, canal_max, canal):
        self.ligada = False
        self.canal = canal
        self.canal_min = canal_min
        self.canal_max = canal_max
    
    def ligando_tv(self):
        self.ligada = not self.ligada  
        status = 'ligada' if self.ligada else 'desligada'
        print(f"A TV foi {status}.")

    def c_baixo(self):
        if self.ligada:
            if self.canal + 1 <= self.canal_max: # DE BAIXO VAI PARA CIMA E CIMA VAI PARA BAIXO
                self.canal += 1 
                return self.canal
            return self.canal
        else:
            print('tv desligada')
    def c_cima(self):
        if self.ligada:
            if self.canal - 1 >= self.canal_min:  # FIZ UMA PEQUENA MUDANÇA NOS METADOS, PARA INVERTER OS VALORES DOS CANAIS 
                    self.canal -= 1 
                    return self.canal
            return self.canal

        else:
            print('tv desligada')
# meu controle
class ControleRemoto:
    def __init__(self, Televisao, Bateria):
        self.Televisao = Televisao
        self.Bateria = Bateria  
    
    def liga(self):
        if self.Bateria.consuma(1):
            self.Televisao.ligada = True
    
    def desliga(self):
        if self.Bateria.consuma(1):
            self.Televisao.ligada = False
    
    def canal_mais(self):
        if self.Bateria.consuma(1):
           self.Televisao.c_baixo()
    
    def canal_menos(self):
        if self.Bateria.consuma(1):
            self.Televisao.c_cima()
# bateria di meu controle
class Bateria:
    def __init__(self, energia=100):
        self.energia = energia
    
    def consuma(self, consumo):
        if consumo > self.energia:
            consumo = self.energia
        self.energia -= consumo
        return consumo


tv = Televisao(2, 14, 2)
tv.ligando_tv()
pilha = Bateria()
controle = ControleRemoto(tv, pilha)
controle.canal_mais()
print(tv.canal)


# for x in range(0, 9):
#     # Tv.c_baixo()
#     print(tv.c_baixo())                

# for x in range(0, 9):
#     # Tv.c_cima()
#     print(tv.c_cima()) 
  
