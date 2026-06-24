# class Contador:
#     instancias = 0
#     def __init__(self):
#         self.contador = 0
#         Contador.instancias += 1
#     def incrementa(self):    
#         self.contador += 1


# a = Contador()
# b = Contador()        
# print(Contador.instancias)

# class Ponto:
#     MAX_X = 500
#     MAX_Y = 250
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# print(Ponto.MAX_X + Ponto.MAX_Y)   
  
class Ponto:
    MAX_X = 500
    MAX_Y = 250

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def de_string(cls, texto):
        x, y = texto.split(",")
        return cls(int(x), int(y))

p = Ponto.de_string("10,20")
print(p.x, p.y)  # 10 20