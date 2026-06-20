class Televisao:
    def __init__(self, canal, polegadas, marca):
        self.ligada = False
        self.canal = canal
        self.polegadas = polegadas
        self.marca = marca
    
    def ligando_tv(self):
        self.ligada = not self.ligada  
        status = 'ligada' if self.ligada else 'desligada'
        print(f"A TV foi {status}.")
    
    def mudar_canal(self, novo_canal):
        if self.ligada:
            self.canal = novo_canal    
            print(f"Canal alterado para {self.canal}.")
        else:
            print("Não é possível mudar de canal: a TV está desligada.")
    
    def exibir_informacoes(self):
        print(f"TV {self.marca} de {self.polegadas} polegadas. Canal atual: {self.canal}.")    

tv = Televisao(canal=2, polegadas=55, marca='samsung')

tv.ligando_tv()
tv.mudar_canal(5)
tv.exibir_informacoes()