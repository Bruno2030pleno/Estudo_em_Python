class Tv:
    
    def __init__(self):
       self.ligada = False
       self.canal = 2
    
    
    def c_baixo(self):
        self.canal -= 1
    def c_cima(self):
        self.canal += 1
        
controle = Tv()
controle.c_cima()
controle.c_baixo()
print(controle.canal)
controle.c_cima()

