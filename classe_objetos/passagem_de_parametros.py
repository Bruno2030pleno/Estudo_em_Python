class Televisao:
    def __init__(self, canal_min, canal_max, canal=2):
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
            if self.canal - 1 >= self.canal_min:  # FIZ UMA PEQUENA MUDANÇA NOS METADOS, PARA IVERTER OS VALORES DOS CANAIS 
                    self.canal -= 1 
                    return self.canal
            return self.canal

        else:
            print('tv desligada') 
# Tv = Televisao()
Tv2 = Televisao(canal_min=0, canal_max=10)
Tv2.ligando_tv()


for x in range(0, 9):
    # Tv.c_baixo()
    print(Tv2.c_baixo())                

for x in range(0, 9):
    # Tv.c_cima()
    print(Tv2.c_cima()) 
  
