from functools import total_ordering

@total_ordering
class TipoTelefone:
    def __init__(self, tipo):
        self.tipo = tipo
    def __str__(self):
        return f"({self.tipo})"
    def __eq__(self, outro):
        if outro is None:
           return False
        return self.tipo == outro.tipo
    def __lt__(self, outro):
        return self.tipo < outro.tipo
    
class Phone:
    def __init__(self, namber, tipo=None):
        self.namber =  namber
        self.tipo = tipo
    def __str__(self):
        tipo = self.tipo or ""
        return f"{self.numero} {tipo}"
    def __eq__(self, outro):
        return self.numero == outro.namber and ((self.tipo == outro.tipo ) or (self.tipo is None or outro.tipo is None))
    @property
    def namber(self):
        return self.__namber
    @namber.setter
    def namber(self, valor):
        if valor is None or not valor.strip():
            raise ValueError("namber não pode ser None ou em branco!!!!! ")
        self.__namber = valor      

                                  
            
        