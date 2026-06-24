from lista_unica import ListaUnica
from tipo_telefone import Phone
from nome import Name

class Phones(ListaUnica):
    def __init__(self):
        super().__init__(Phone)

class DadoAgenda:
    def __init__(self, name):
        self.name = name
        self.phones = Phones()
    @property
    def name(self):
        return self.__name 
    @name.setter
    
    def name(self, valor):
        if not isinstance(valor, Name):
            raise TypeError("name deve ser uma instãncia da classe name")
        self.__name = valor
    
    def pesquisaPhone(self, telefone):
        posição = self.phones.pesquisa(Phone(telefone))
        if posição == -1:
            return None
        return self.phones[posição]            
            