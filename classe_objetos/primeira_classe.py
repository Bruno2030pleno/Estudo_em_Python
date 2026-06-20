class Carro:
    def __init__(self, marca, velocidade):
        self.marca = marca
        self.velocidade = velocidade

    def acelerar(self):
        print(f"{self.marca} está acelerando a {self.velocidade} km/h!")

# Objetos criados FORA da classe
carro1 = Carro("Ford", 80)
carro2 = Carro("BMW", 120)

print(carro1.marca)    # Ford
carro2.acelerar()      # BMW está acelerando a 120 km/h!